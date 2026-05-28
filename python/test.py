import aiohttp
import asyncio

async def main():
    api_key ='sk_zcgG9wdh7dwV2rSFdRk57zZ6SweR4xuB'
    prompt = 'a futuristic cityscape at sunset, with flying cars and neon lights'
    url = f'https://image.pollinations.ai/prompt/{prompt.replace(" ", "%20")}?key={api_key}'
    
    
    api_key2 = 'pub_9142a14c1e234140a1c320a60d408267'
    url2 = f"https://newsdata.io/api/1/latest?apikey={api_key2}&size=5&language=en"
    #handle two urls in async way
    urls = [url, url2]
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(f"Fetching data from: {url}🌐")
                if url == url2:
                    data = await response.json()
                    for i, article in enumerate(data['results']):
                        i += 1
                        print('=' * 50)
                        print(f"{i}. {article['title']}")
                        print(f"    {article['link'].replace(' ', '/' )}")
                        print(f"   {article['pubDate']}")
                        print("=" * 50 + '\n')
                        
                        
                else:
                    image_data = await response.read()
                    with open('generated_image.png', 'wb') as f:
                        f.write(image_data)
                    print("image successfully generated ✅")

if __name__ == "__main__":
    asyncio.run(main())
