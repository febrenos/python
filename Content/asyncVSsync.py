import asyncio
import time
COLOR_GREEN = '\033[92m'
COLOR_RESET = '\033[0m'

# Código assíncrono usando asyncio
async def async_task1():
    print("-> Start async_task1()")
    await asyncio.sleep(3)
    print("-> End async_task1()")
    return "async_task1 ready"

async def async_task2():
    print("-> Start async_task2()")
    await asyncio.sleep(2)
    print("-> End async_task2()")
    return "async_task2 ready"

async def main_async():
    start_time = time.time()

    result_async_task1, result_async_task2 = await asyncio.gather(async_task1(), async_task2())

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Result of async_task1: {result_async_task1}")
    print(f"Result of async_task2: {result_async_task2}")
    print(f"Total execution ASYNC: {COLOR_GREEN}{elapsed_time:.2f} seconds {COLOR_RESET}")

# Código síncrono usando time.sleep()
def sync_task1():
    print("-> Start sync_task1()")
    time.sleep(3)
    print("-> End sync_task1()")
    return "sync_task1 ready"

def sync_task2():
    print("-> Start sync_task2()")
    time.sleep(2)
    print("-> End sync_task2()")
    return "sync_task2 ready"

def main_sync():
    start_time = time.time()
    result_sync_task1 = sync_task1()
    result_sync_task2 = sync_task2()
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"Result of sync_task1: {result_sync_task1}")
    print(f"Result of sync_task2: {result_sync_task2}")
    print(f"Total execution SYNC: {COLOR_GREEN}{elapsed_time:.2f} seconds{COLOR_RESET}")

if __name__ == "__main__":
    print(f"\n{COLOR_GREEN}>>> Running ASYNCHRONOUS:{COLOR_RESET}")
    asyncio.run(main_async())

    print(f"\n{COLOR_GREEN}>>> Running SYNCHRONOUS:{COLOR_RESET}")
    main_sync()
