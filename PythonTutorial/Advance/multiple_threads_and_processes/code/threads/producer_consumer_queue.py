import concurrent.futures
import logging
import queue
import random
import threading


def producer(queue, event):
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())

    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format_time = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format_time, level=logging.INFO, datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # time.sleep(5)
        # logging.info("Main: about to set event")
        event.set()
# 让我们从 "事件 "开始。threading.Event对象允许一个线程发出事件信号，而其他许多线程可以等待该事件的发生。这段代码中的关键用法是，
# 等待事件发生的线程不一定需要停止正在做的事情，它们只需每隔一段时间检查一下Event的状态。
# 生产者在消费者运行之前就已经得到了两条消息。如果你回头看看生产者和.set_message()，你会注意到它唯一会等待锁的地方是当它试图将消息放入管道时。这是在生产者得到消息并记录下它拥有消息后进行的。
#
# 当生产者试图发送这第二条消息时，它将第二次调用.set_message()，并且会阻塞。
#
# 操作系统可以在任何时候交换线程，但它通常会让每个线程有合理的运行时间，然后再将其交换出去。这就是为什么生产者通常会运行到第二次调用.set_message()时阻塞。
#
# 然而，一旦一个线程被阻塞，操作系统总是会把它换出来，并找到一个不同的线程来运行。在这种情况下，唯一有事情可做的其他线程就是消费者。
#
# 消费者调用.get_message()，读取消息并调用.producer_lock的.release()，从而允许生产者在下次线程交换时再次运行。
#
# 请注意，第一条消息是43，这正是消费者读取的内容，尽管生产者已经生成了45条消息。
#
# 虽然它在这个有限的测试中是有效的，但在一般情况下，它并不是解决生产者-消费者问题的好办法，因为它一次只允许管道中的一个值。当生产者得到大量的消息时，它将没有地方可以放置它们。
#
# 让我们继续用一个更好的方法来解决这个问题，即使用队列。
