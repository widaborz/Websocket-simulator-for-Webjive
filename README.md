#### Changes on Webjive:

On file: *webjive/src/dashboard/components/RunCanvas/emmiter.ts* 
 
Change:
```
function createSocket(tangoDB: string) {
  return new WebSocket(socketUrl(tangoDB), "graphql-ws");
}
```
To:
```
function createSocket(tangoDB: string) {
  var wsUri = "ws://127.0.0.1:1234/websocketserver";
  return new WebSocket(wsUri);
}
```

On file:  *webjive/src/jive/state/api/tango/index.js*

Change:
```
function createSocket(tangoDB) {
  return new WebSocket(socketUrl(tangoDB), "graphql-ws");
}
```
To:
```
function createSocket(tangoDB) {
  var wsUri = "ws://127.0.0.1:1234/websocketserver";
  return new WebSocket(wsUri);
}
```

## Install:

```
pip install tornado
```

## Configuration:

On file: *websocket.py* change the values: 


```
num_message = 100
time = 0.1
```

*num_message* is the number of message to send to the websocket. 
*time* is the time between two messages (in seconds)

## Run:

```
python3 websocket.py
```


