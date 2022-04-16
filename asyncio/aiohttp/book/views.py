import asyncio
import time

import aiohttp
import requests
from django.shortcuts import render
import json

# def example(request):

#     starting_time = time.time()

#     pokemon_data = []

#     for num in range(1, 50):
#         url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#         url = "https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendMessage?chat_id=299470913&text=hello"
#         res = requests.get(url)
#         pokemon = res.json()
#         #print(pokemon)
#         #pokemon_data.append(pokemon["name"])

#     count = len(pokemon_data)
#     total_time = time.time() - starting_time

#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )


# async def example(request):

#     starting_time = time.time()

#     pokemon_data = []

#     async with aiohttp.ClientSession() as session:
#         for num in range(1, 101):
#             #pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#             pokemon_url = "https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendMessage?chat_id=299470913&text=hello"
#             async with session.get(pokemon_url) as res:
#                 #pokemon = await res.json()
#                 print("hey")
#                 #pokemon_data.append(pokemon["name"])

#     count = 1
#     total_time = time.time() - starting_time

#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )
    
################################
# async def example(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://catfact.ninja/fact") as res:
#             data = await res.json()
#             print(data)
    
#     return render(request, "index.html", {
#         "data":data,
#     })
        
########################


# async def example(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://pokeapi.co/api/v2/pokemon/1") as res:
#             data = await res.json()
#             print(data)

#     return render(request, "index.html", {
#         "data": data,
#     })


            

# async def get_pokemon(session, url):
#     async with session.get(url) as res:
#         pokemon_data = await res.json()
#         return pokemon_data


# async def example(request):

#     starting_time = time.time()

#     actions = []
#     pokemon_data = []

#     async with aiohttp.ClientSession() as session:
#         for num in range(1, 77):
#             url = f"https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendMessage?chat_id=299470913&text=hello"
#             actions.append(asyncio.ensure_future(get_pokemon(session, url)))

#         pokemon_res = await asyncio.gather(*actions)
#         # for data in pokemon_res:
#         #     pokemon_data.append(data)

#     count = len(pokemon_data)
#     total_time = time.time() - starting_time

#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
    # )


# async def example(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://pokeapi.co/api/v2/pokemon/1") as res:
#             data = await res.json()
#             print(data)

#     return render(
#         request,
#         "index.html",
#         {"data": data},
#     )



########## 
# 21секунду - 100штук !!!!!!!!!!
# async def example(request):
#     starting_time = time.time()
#     pokemon_data = []
    
#     async with aiohttp.ClientSession() as session:
#         for num in range(1,101):
#             pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#             pokemon_url = f"https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendMessage?chat_id=299470913&text=hello"
#             async with session.get(pokemon_url) as res:
#                 #pokemon = await res.json()  ### здесь плохо то что мы ждем
#                 print(res)
#                 #pokemon_data.append(pokemon["name"])
                
#     count = len(pokemon_data)
#     total_time = time.time() - starting_time
    
#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )

imgurl_sender = f"https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendPhoto?chat_id=299470913&photo=https://zooblog.ru/wp-content/uploads/2021/02/picture-13-4.jpeg"

###############
# одновременная отправа .gather

async def url_sender(session, url):
    async with session.get(url) as res:
        task_sender_data = await res.json()
        print("------------------------------------------------")
        print(task_sender_data)
        print("------------------------------------------------")
        return task_sender_data



async def example(request):
    
    starting_time = time.time()
    task_sender_data = []
    actions = []
    users = ["299470913", "5033498348", "913592295", "675044345" ] 
    text = "*bold* hello not bold _italic_"
    parse_mode = "markdown"
    async with aiohttp.ClientSession() as session:
        for user in users:
            url = f"https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendMessage?chat_id={user}&text={text}&parse_mode={parse_mode}"
            actions.append(asyncio.ensure_future(url_sender(session, url)))

        task_sender_data_result = await asyncio.gather(*actions)
        for data in task_sender_data_result:
            task_sender_data.append(data)


    count = len(task_sender_data)
    total_time = time.time() - starting_time
    
    false = 0
    for i in task_sender_data:
        if i["ok"] == False:
            false += 1

    count = count - false
        
    
    return render(
        request,
        "index.html",
        {"data": task_sender_data, "count": count, "time": total_time},
    )

#https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendAudio?chat_id=5033498348&audio=https://5a73-89-222-217-38.ngrok.io/documents/documents/Numb.mp3

#https://api.telegram.org/bot2027308400:AAGfchrhWkd5eFxQ_K9UB6G_Im8MS1zUM9A/sendAudio?chat_id=299470913&audio=https://5a73-89-222-217-38.ngrok.io/documents/documents/Numb.mp3
