import asyncio

async def writer(write_queue):
    for i in range(1, 11):
        message = f"Writing: {i}"
        print(message)
        await write_queue.put(i)
        await asyncio.sleep(0.5)

async def reader(write_queue):
    while True:
        data = await write_queue.get()
        if data is None:
            break
        message = f"Reading: {data}"
        print(message)

async def main():
    write_queue = asyncio.Queue()
    
    # Create tasks for writer and reader
    writer_task = asyncio.create_task(writer(write_queue))
    reader_task = asyncio.create_task(reader(write_queue))
    
    # Wait for writer to finish
    await writer_task
    
    # Signal reader to stop
    await write_queue.put(None)
    await reader_task

asyncio.run(main())
