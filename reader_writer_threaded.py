import threading
import asyncio

async def writer(write_queue):
    for i in range(1, 11):
        print("Writing:", i)
        await write_queue.put(i)
        await asyncio.sleep(0.5)

async def reader(write_queue):
    while True:
        data = await write_queue.get()
        if data is None:
            break
        print("Reading:", data)

async def main():
    write_queue = asyncio.Queue()
    
    # Create a new thread for the reader
    loop = asyncio.get_event_loop()
    reader_task = loop.create_task(reader(write_queue))
    
    # Writer runs within the main thread
    await writer(write_queue)
    
    # Signal reader to stop
    await write_queue.put(None)
    
    # Wait for the reader task to finish
    await reader_task

asyncio.run(main())
