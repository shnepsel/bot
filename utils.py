# import openai as novaai

# novaai.api_base = 'https://api.nova-oss.com/v1'

# novaai.api_key = 'nv-Nv2gAX8KUngO7nXfTF2RN0V4x0SSHddD2YpET4wpYPv6qd3n'

import openai as novaai
import logging
import config

novaai.api_key = config.novaai.api_key

async def generate_text(prompt) -> dict:
    try:
        response = await novaai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'], response['usage']['total_tokens']
    except Exception as e:
        logging.error(e)
   
async def generate_image(prompt, n=1, size="1024x1024") -> list[str]:
    try:
        response = await novaai.Image.acreate(
            prompt=prompt,
            n=n,
            size=size
        )
        urls = []
        for i in response['data']:
            urls.append(i['url'])
    except Exception as e:
        logging.error(e)
        return []
    else:
        return urls