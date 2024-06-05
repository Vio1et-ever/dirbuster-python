import requests
import asyncio

data = []

async def async_url_fuzz_test(url, wordlist, filetype, output_text):
    with open(wordlist, 'r') as f:
        for line in f:
            directory = line.strip()
            if '#' in directory:
                continue
            full_url = "{}/{}.{}".format(url, directory, filetype)
            response = await asyncio.get_event_loop().run_in_executor(None, requests.get, full_url)
            if response.status_code == 200:
                found_message = f"Directory found: {full_url}\n"
                output_text.insert('end', found_message)
                data.append(full_url)

async def async_dirbuster(url, wordlist, filetypes, savefile, output_text):
    tasks = [async_url_fuzz_test(url, wordlist, f, output_text) for f in filetypes]
    await asyncio.gather(*tasks)
    if savefile:
        with open(savefile, 'w') as f:
            for item in data:
                f.write(item + '\n')