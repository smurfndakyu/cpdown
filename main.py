import requests
import asyncio
import aiohttp
import json
import zipfile
from typing import Dict, List, Any, Tuple
from collections import defaultdict
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64
from pyrogram import Client, filters
import sys
import re
import requests
import uuid
import random
import string
import hashlib
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.enums import ChatMemberStatus
from pyrogram.raw.functions.channels import GetParticipants
from config import api_id, api_hash, bot_token, auth_users
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor
THREADPOOL = ThreadPoolExecutor(max_workers=1000)
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the bot_link at the beginning of your script
bot_link = "http://t.me/Bhumihar_PWEXT_bot"  

           
#image_list = [
#"https://graph.org/file/996d4fc24564509244988-a7d93d020c96973ba8.jpg",
#"https://graph.org/file/96d25730136a3ea7e48de-b0a87a529feb485c8f.jpg",
#"https://graph.org/file/6593f76ddd8c735ae3ce2-ede9fa2df40079b8a0.jpg",
#"https://graph.org/file/a5dcdc33020aa7a488590-79e02b5a397172cc35.jpg",
#"https://graph.org/file/0346106a432049e391181-7560294e8652f9d49d.jpg",
#]
#print(4321)
bot = Client(
    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)

#@bot.on_message(filters.command(["start"]))
#async def start(bot, message):
  #random_image_url = random.choice(image_list)

  #keyboard = [
    #[
      #InlineKeyboardButton("🚀 ᴘᴡ ᴡɪᴛʜᴏᴜᴛ ᴘᴜʀᴄʜᴀsᴇ 🚀", callback_data="pwwp")
    #]
  #]

  #reply_markup = InlineKeyboardMarkup(keyboard)
  #await message.reply_photo(
    #photo=random_image_url,
    #caption="☆ ɪ ᴀᴍ ᴛxᴛ ᴇxᴛʀᴀᴄᴛᴏʀ ʙᴏᴛ.\n\n☆ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ ᴛᴜsʜᴀʀ.\n\n☆ ᴘʟᴇᴀsᴇ ᴘʀᴇss ᴅᴏᴡɴ.",
    #quote=True,
    #reply_markup=reply_markup
#)


# Inline keyboard for start command
keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑🗿" ,url=f"https://t.me/Thebhumihar") ],
                    [
                    InlineKeyboardButton("🔔𝐔𝐏𝐃𝐀𝐓𝐄 𝐂𝐇𝐀𝐍𝐍𝐄𝐋🔔" ,url="https://t.me/BHUMIHAR_BOTSS") ],
                    [
                    InlineKeyboardButton("🚀ᴘᴡ ᴡɪᴛʜᴏᴜᴛ ᴘᴜʀᴄʜᴀsᴇ🚀", callback_data="pwwp")                              
                ],           
            ]
      )
    
# Image URLs for the random image feature
image_urls = [
    "https://graph.org/file/996d4fc24564509244988-a7d93d020c96973ba8.jpg",
    "https://graph.org/file/96d25730136a3ea7e48de-b0a87a529feb485c8f.jpg",
    "https://graph.org/file/6593f76ddd8c735ae3ce2-ede9fa2df40079b8a0.jpg",
    "https://graph.org/file/a5dcdc33020aa7a488590-79e02b5a397172cc35.jpg",
    "https://graph.org/file/0346106a432049e391181-7560294e8652f9d49d.jpg",
    "https://graph.org/file/ba49ebe9a8e387addbcdc-be34c4cd4432616699.jpg",
    "https://graph.org/file/26f98dec8b3966687051f-557a430bf36b660e24.jpg",
    "https://graph.org/file/2ae78907fa4bbf3160ffa-2d69cd23fa75cb0c3a.jpg",
    "https://graph.org/file/05ef9478729f165809dd7-3df2f053d2842ed098.jpg",
    "https://graph.org/file/b1330861fed21c4d7275c-0f95cca72c531382c1.jpg",
    "https://graph.org/file/0ebb95807047b062e402a-9e670a0821d74e3306.jpg",
    "https://graph.org/file/b4e5cfd4932d154ad6178-7559c5266426c0a399.jpg",
    "https://graph.org/file/44ffab363c1a2647989bc-00e22c1e36a9fd4156.jpg",
    "https://graph.org/file/5f0980969b54bb13f2a8a-a3e131c00c81c19582.jpg",
    "https://graph.org/file/6341c0aa94c803f94cdb5-225b2999a89ff87e39.jpg",
    "https://graph.org/file/90c9f79ec52e08e5a3025-f9b73e9d17f3da5040.jpg",
    "https://graph.org/file/1aaf27a49b6bd81692064-30016c0a382f9ae22b.jpg",
    "https://graph.org/file/702aa31236364e4ebb2be-3f88759834a4b164a0.jpg",
    "https://graph.org/file/d0c6b9f6566a564cd7456-27fb594d26761d3dc0.jpg",
    # Add more image URLs as needed
]
random_image_url = random.choice(image_urls) 
# Caption for the image
caption = (
        "**𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫 👋!**\n\n"
        "➠ **𝐈 𝐚𝐦 𝐚 𝐓𝐞𝐱𝐭 𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐨𝐫 𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐛𝐲 𝗕𝗛𝗨𝗠𝗜𝗛𝗔𝗥**\n"
        "➠ ** 𝐈 𝐂𝐚𝐧 𝐄𝐱𝐭𝐫𝐚𝐜𝐭 𝐓𝐱𝐭 𝐅𝐢𝐥𝐞 𝐎𝐟 𝐏𝐖 𝐁𝐚𝐭𝐜𝐡𝐞𝐬**\n\n"
        "➠ **𝐌𝐚𝐝𝐞 𝐁𝐲:** 🇧 🇭 🇺 🇲 🇮 🇭 🇦 🇷 "
)
    
# Start command handler
@bot.on_message(filters.command(["start"]))
async def start_command(bot: Client, message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo=random_image_url, caption=caption, reply_markup=keyboard)
    

 
 
@bot.on_message(group=2)
#async def account_login(bot: Client, m: Message):
#    try:
#        await bot.forward_messages(chat_id=chat_id, from_chat_id=m.chat.id, message_ids=m.id)
#    except:
#        pass
        
async def fetch_pwwp_data(session: aiohttp.ClientSession, url: str, headers: Dict = None, params: Dict = None, data: Dict = None, method: str = 'GET') -> Any:
    max_retries = 3
    for attempt in range(max_retries):
        try:
            async with session.request(method, url, headers=headers, params=params, json=data) as response:
                response.raise_for_status()
                return await response.json()
        except aiohttp.ClientError as e:
            logging.error(f"Attempt {attempt + 1} failed: aiohttp error fetching {url}: {e}")
        except Exception as e:
            logging.exception(f"Attempt {attempt + 1} failed: Unexpected error fetching {url}: {e}")

        if attempt < max_retries - 1:
            await asyncio.sleep(90 ** attempt)
        else:
            logging.error(f"Failed to fetch {url} after {max_retries} attempts.")
            return None


async def process_pwwp_chapter_content(session: aiohttp.ClientSession, chapter_id, selected_batch_id, subject_id, schedule_id, content_type, headers: Dict):
    url = f"https://api.penpencil.co/v1/batches/{selected_batch_id}/subject/{subject_id}/schedule/{schedule_id}/schedule-details"
    data = await fetch_pwwp_data(session, url, headers=headers)
    content = []

    if data and data.get("success") and data.get("data"):
        data_item = data["data"]

        if content_type in ("videos", "DppVideos"):
            video_details = data_item.get('videoDetails', {})
            if video_details:
                name = data_item.get('topic', '')
                videoUrl = video_details.get('videoUrl') or video_details.get('embedCode') or ""
            #    image = video_details.get('image', "")

                if videoUrl:
                    line = f"{name}:{videoUrl}"
                    content.append(line)
               #     logging.info(line)

        elif content_type in ("notes", "DppNotes"):
            homework_ids = data_item.get('homeworkIds', [])
            for homework in homework_ids:
                attachment_ids = homework.get('attachmentIds', [])
                name = homework.get('topic', '')
                for attachment in attachment_ids:
                    url = attachment.get('baseUrl', '') + attachment.get('key', '')
                    if url:
                        line = f"{name}:{url}"
                        content.append(line)
                    #    logging.info(line)

        return {content_type: content} if content else {}
    else:
        logging.warning(f"No Data Found For  Id - {schedule_id}")
        return {}


async def fetch_pwwp_all_schedule(session: aiohttp.ClientSession, chapter_id, selected_batch_id, subject_id, content_type, headers: Dict) -> List[Dict]:
    all_schedule = []
    page = 1
    while True:
        params = {
            'tag': chapter_id,
            'contentType': content_type,
            'page': page
        }
        url = f"https://api.penpencil.co/v2/batches/{selected_batch_id}/subject/{subject_id}/contents"
        data = await fetch_pwwp_data(session, url, headers=headers, params=params)

        if data and data.get("success") and data.get("data"):
            for item in data["data"]:
                item['content_type'] = content_type
                all_schedule.append(item)
            page += 1
        else:
            break
    return all_schedule


async def process_pwwp_chapters(session: aiohttp.ClientSession, chapter_id, selected_batch_id, subject_id, headers: Dict):
    content_types = ['videos', 'notes', 'DppNotes', 'DppVideos']
    
    all_schedule_tasks = [fetch_pwwp_all_schedule(session, chapter_id, selected_batch_id, subject_id, content_type, headers) for content_type in content_types]
    all_schedules = await asyncio.gather(*all_schedule_tasks)
    
    all_schedule = []
    for schedule in all_schedules:
        all_schedule.extend(schedule)
        
    content_tasks = [
        process_pwwp_chapter_content(session, chapter_id, selected_batch_id, subject_id, item["_id"], item['content_type'], headers)
        for item in all_schedule
    ]
    content_results = await asyncio.gather(*content_tasks)

    combined_content = {}
    for result in content_results:
        if result:
            for content_type, content_list in result.items():
                if content_type not in combined_content:
                    combined_content[content_type] = []
                combined_content[content_type].extend(content_list)

    return combined_content


async def get_pwwp_all_chapters(session: aiohttp.ClientSession, selected_batch_id, subject_id, headers: Dict):
    all_chapters = []
    page = 1
    while True:
        url = f"https://api.penpencil.co/v2/batches/{selected_batch_id}/subject/{subject_id}/topics?page={page}"
        data = await fetch_pwwp_data(session, url, headers=headers)

        if data and data.get("data"):
            chapters = data["data"]
            all_chapters.extend(chapters)
            page += 1
        else:
            break

    return all_chapters


async def process_pwwp_subject(session: aiohttp.ClientSession, subject: Dict, selected_batch_id: str, selected_batch_name: str, zipf: zipfile.ZipFile, json_data: Dict, all_subject_urls: Dict[str, List[str]], headers: Dict):
    subject_name = subject.get("subject", "Unknown Subject").replace("/", "-")
    subject_id = subject.get("_id")
    json_data[selected_batch_name][subject_name] = {}
    zipf.writestr(f"{subject_name}/", "")
    
    chapters = await get_pwwp_all_chapters(session, selected_batch_id, subject_id, headers)
    
    chapter_tasks = []
    for chapter in chapters:
        chapter_name = chapter.get("name", "Unknown Chapter").replace("/", "-")
        zipf.writestr(f"{subject_name}/{chapter_name}/", "")
        json_data[selected_batch_name][subject_name][chapter_name] = {}

        chapter_tasks.append(process_pwwp_chapters(session, chapter["_id"], selected_batch_id, subject_id, headers))

    chapter_results = await asyncio.gather(*chapter_tasks)

    all_urls = []
    for chapter, chapter_content in zip(chapters, chapter_results):
        chapter_name = chapter.get("name", "Unknown Chapter").replace("/", "-")

        for content_type in ['videos', 'notes', 'DppNotes', 'DppVideos']:
            if chapter_content.get(content_type):
                content = chapter_content[content_type]
                content.reverse()
                content_string = "\n".join(content)
                zipf.writestr(f"{subject_name}/{chapter_name}/{content_type}.txt", content_string.encode('utf-8'))
                json_data[selected_batch_name][subject_name][chapter_name][content_type] = content
                all_urls.extend(content)
    all_subject_urls[subject_name] = all_urls

def find_pw_old_batch(batch_search):

    try:
        response = requests.get(f"https://abhiguru143.github.io/AS-MULTIVERSE-PW/batch/batch.json")
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
        return []

    matching_batches = []
    for batch in data:
        if batch_search.lower() in batch['batch_name'].lower():
            matching_batches.append(batch)

    return matching_batches

@bot.on_callback_query(filters.regex("^pwwp$"))
async def pwwp_callback(bot, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.answer()
    
    if user_id not in auth_users:
        await bot.send_message(callback_query.message.chat.id, f"**𝐘𝐎𝐔 𝐀𝐑𝐄 𝐍𝐎𝐓 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐔𝐒𝐄𝐑 \n 𝐅𝐎𝐑 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐓𝐎 𝐁𝐎𝐓 𝐎𝐖𝐍𝐄𝐑.**")
        return
        
    THREADPOOL.submit(asyncio.run, process_pwwp(bot, callback_query.message, user_id, "http://t.me/Bhumihar_PWEXT_bot"))

async def process_pwwp(bot: Client, m: Message, user_id: int, bot_link: str):

    
        raw_text1 = ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU2NzIzMjkuNDQ1LCJkYXRhIjp7Il9pZCI6IjY1NzY4MGFiYWMxYmVkMDAxOGVhN2FjNSIsInVzZXJuYW1lIjoiODg1MTk1MDE5NyIsImZpcnN0TmFtZSI6IkFuc2hpdCIsImxhc3ROYW1lIjoiU2luZ2giLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwicm9sZXMiOlsiNWIyN2JkOTY1ODQyZjk1MGE3NzhjNmVmIl0sImNvdW50cnlHcm91cCI6IklOIiwidHlwZSI6IlVTRVIifSwiaWF0IjoxNzQ1MDY3NTI5fQ.ICskFElSKuwF9rYGDvi99eXZhw5-SKvx4tWDONlFZjE")
    

    headers = {
        'Host': 'api.penpencil.co',
        'client-id': '5eb393ee95fab7468a79d189',
        'client-version': '1910',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2101K6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'randomid': '72012511-256c-4e1c-b4c7-29d67136af37',
        'client-type': 'WEB',
        'content-type': 'application/json; charset=utf-8',
    }
     

    loop = asyncio.get_event_loop()    
    CONNECTOR = aiohttp.TCPConnector(limit=1000, loop=loop)
    async with aiohttp.ClientSession(connector=CONNECTOR, loop=loop) as session:
        try:
            if raw_text1.isdigit() and len(raw_text1) == 10:
                phone = raw_text1
                data = {
                    "username": phone,
                    "countryCode": "+91",
                    "organizationId": "5eb393ee95fab7468a79d189"
                }
                try:
                    async with session.post(f"https://api.penpencil.co/v1/users/get-otp?smsType=0", json=data, headers=headers) as response:
                        await response.read()
                    
                except Exception as e:
                    await editable.edit(f"**Error : {e}**")
                    return

                editable = await editable.edit("**ENTER OTP YOU RECEIVED**")
                try:
                    input2 = await bot.listen(chat_id=m.chat.id, filters=filters.user(user_id), timeout=120)
                    otp = input2.text
                    await input2.delete(True)
                except:
                    await editable.edit("**Timeout! You took too long to respond**")
                    return

                payload = {
                    "username": phone,
                    "otp": otp,
                    "client_id": "system-admin",
                    "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
                    "grant_type": "password",
                    "organizationId": "5eb393ee95fab7468a79d189",
                    "latitude": 0,
                    "longitude": 0
                }

                try:
                    async with session.post(f"https://api.penpencil.co/v3/oauth/token", json=payload, headers=headers) as response:
                        access_token = (await response.json())["data"]["access_token"]
                        monster = await editable.edit(f"<b>Physics Wallah Login Successful ✅</b>\n\n<pre language='Save this Login Token for future usage'>{access_token}</pre>\n\n")
                        editable = await m.reply_text("**Getting Batches In Your I'd**")
                    
                except Exception as e:
                    await editable.edit(f"**Error : {e}**")
                    return

            else:
                access_token = raw_text1
            
            headers['authorization'] = f"Bearer {access_token}"
        
            params = {
                'mode': '1',
                'page': '1',
            }
            try:
                async with session.get(f"https://api.penpencil.co/v3/batches/all-purchased-batches", headers=headers, params=params) as response:
                    response.raise_for_status()
                    batches = (await response.json()).get("data", [])
            except Exception as e:
                await editable.edit("**```\nLogin Failed❗TOKEN IS EXPIRED```\nPlease Enter Working Token\n                       OR\nLogin With Phone Number**")
                return
        
            await editable.edit("**Enter Your Batch Name**")
            try:
                input3 = await bot.listen(chat_id=m.chat.id, filters=filters.user(user_id), timeout=120)
                batch_search = input3.text
                await input3.delete(True)
            except:
                await editable.edit("**Timeout! You took too long to respond**")
                return
                
            url = f"https://api.penpencil.co/v3/batches/search?name={batch_search}"
            courses = await fetch_pwwp_data(session, url, headers)
            courses = courses.get("data", {}) if courses else {}

            if courses:
                text = ''
                for cnt, course in enumerate(courses):
                    name = course['name']
                    text += f"{cnt + 1}. ```\n{name}```\n"
                await editable.edit(f"**Send index number of the course to download.\n\n{text}\n\nIf Your Batch Not Listed Above Enter - No**")
            
                try:
                    input4 = await bot.listen(chat_id=m.chat.id, filters=filters.user(user_id), timeout=120)
                    raw_text4 = input4.text
                    await input4.delete(True)
                except:
                    await editable.edit("**Timeout! You took too long to respond**")
                    return
                
                if input4.text.isdigit() and 1 <= int(input4.text) <= len(courses):
                    selected_course_index = int(input4.text.strip())
                    course = courses[selected_course_index - 1]
                    selected_batch_id = course['_id']
                    selected_batch_name = course['name']
                    clean_batch_name = selected_batch_name.replace("/", "-").replace("|", "-")
                    clean_file_name = f"{user_id}_{clean_batch_name}"
                    
                elif "No" in input4.text:
                    courses = find_pw_old_batch(batch_search)
                    if courses:
                        text = ''
                        for cnt, course in enumerate(courses):
                            name = course['batch_name']
                            text += f"{cnt + 1}. ```\n{name}```\n"
                            
                        await editable.edit(f"**Send index number of the course to download.\n\n{text}**")
                
                        try:
                            input5 = await bot.listen(chat_id=m.chat.id, filters=filters.user(user_id), timeout=120)
                            raw_text5 = input5.text
                            await input5.delete(True)
                        except:
                            await editable.edit("**Timeout! You took too long to respond**")
                            return
                
                        if input5.text.isdigit() and 1 <= int(input5.text) <= len(courses):
                            selected_course_index = int(input5.text.strip())
                            course = courses[selected_course_index - 1]
                            selected_batch_id = course['batch_id']
                            selected_batch_name = course['batch_name']
                            clean_batch_name = selected_batch_name.replace("/", "-").replace("|", "-")
                            clean_file_name = f"{user_id}_{clean_batch_name}"
                        else:
                            raise Exception("Invalid batch index.")
                else:
                    raise Exception("Invalid batch index.")
                    
                await editable.edit(f"**Extracting course : {selected_batch_name} ...**")
                  
                start_time = time.time()
                
                url = f"https://api.penpencil.co/v3/batches/{selected_batch_id}/details"
                batch_details = await fetch_pwwp_data(session, url, headers=headers)

                if batch_details and batch_details.get("success"):
                    subjects = batch_details.get("data", {}).get("subjects", [])

                    json_data = {selected_batch_name: {}}
                    all_subject_urls = {}

                    with zipfile.ZipFile(f"{clean_file_name}.zip", 'w') as zipf:
                        zipf.writestr("Telegram Bot/Extractor Bot.txt", f"Extractor Bot:{bot_link}")
                            
                        subject_tasks = [process_pwwp_subject(session, subject, selected_batch_id, selected_batch_name, zipf, json_data, all_subject_urls, headers) for subject in subjects]
                        await asyncio.gather(*subject_tasks)
                        
                    json_data[selected_batch_name]["Telegram Bot"] = {"Extractor Bot": bot_link}
                    with open(f"{clean_file_name}.json", 'w') as f:
                        json.dump(json_data, f, indent=4)
                            
                    with open(f"{clean_file_name}.txt", 'w', encoding='utf-8') as f:
                        f.write(f"Extractor Bot:{bot_link}\n")
                        for subject in subjects:
                            subject_name = subject.get("subject", "Unknown Subject").replace("/", "-")
                            if subject_name in all_subject_urls:
                                f.write('\n'.join(all_subject_urls[subject_name]) + '\n')
                                    
                    end_time = time.time()
                    response_time = end_time - start_time
                    minutes = int(response_time // 60)
                    seconds = int(response_time % 60)

                    if minutes == 0:
                        if seconds < 1:
                               formatted_time = f"{response_time:.2f} seconds"
                        else:
                            formatted_time = f"{seconds} seconds"
                    else:
                        formatted_time = f"{minutes} minutes {seconds} seconds"
                            
                    await editable.delete(True)
                                
                         
                    caption = f"**Batch Name : ```\n{selected_batch_name}``````\nTime Taken : {formatted_time}``````\nExtracted By : 𝗕𝗛𝗨𝗠𝗜𝗛𝗔𝗥```**"
                                
                    files = [f"{clean_file_name}.{ext}" for ext in ["txt", "zip", "json"]]
                    for file in files:
                        file_ext = os.path.splitext(file)[1][1:]
                        try:
                            with open(file, 'rb') as f:
                                doc = await m.reply_document(document=f, caption=caption, file_name=f"{clean_batch_name}.{file_ext}")
                        except FileNotFoundError:
                            logging.error(f"File not found: {file}")
                        except Exception as e:
                            logging.exception(f"Error sending document {file}:")
                        finally:
                            try:
                                os.remove(file)
                            except OSError as e:
                                logging.error(f"Error deleting {file}: {e}")
                                
                else:
                    raise Exception(f"Error fetching batch details: {batch_details.get('message')}")
            else:
                raise Exception("No batches found for the given search name.")


        except Exception as e:
            logging.exception(f"An unexpected error occurred: {e}")
            try:
                await editable.edit(f"**Error : {e}**")
            except Exception as ee:
                logging.error(f"Failed to send error message to user in callback: {ee}")
        finally:
            if session:
                await session.close()
            await CONNECTOR.close()
            
bot.run()
