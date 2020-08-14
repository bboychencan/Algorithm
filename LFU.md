# LFU

基本思想
- HashMap + 双向链表
- 为了区分频次，需要对每个频次有一个专门的链表
- 这样在进行操作的时候
- 也可以不用链表，直接使用linkedhashset，更加方便。

docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    --volume=$HOME/neo4j/logs:/logs \
    --env=NEO4J_AUTH=neo4j/newpassword \
    --user="$(id -u):$(id -g)" \
    neo4j:latest