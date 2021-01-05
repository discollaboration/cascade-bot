from aiohttp import ClientSession

from config.config import rapidapi_token


class AIOTTS:
    def __init__(self):
        self.sess = ClientSession()

    async def request(self, text: str, outfile: str):
        if self.sess.closed:
            self.sess = ClientSession()
        data = {"text":text,"character":"GLaDOS","emotion":"Contextual","use_diagonal":True}
        async with self.sess.post("https://api.15.ai/app/getAudioFile", json=data) as resp:
            resp.raise_for_status()
            with open(outfile, 'wb') as f:
                f.write(await resp.read())
        return True
