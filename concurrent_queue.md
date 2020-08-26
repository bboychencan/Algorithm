# 并发队列

在分布式场景下，尤其是生产者，消费者模型，queue的使用很常见，这个时候为了保证线程安全需要专门的queue。

java里有BlockingQueue 和 ConcurrentQueue