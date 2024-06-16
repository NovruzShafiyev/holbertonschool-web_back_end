import { queryAPI, weakMap } from "./100-weak.js";

const endpoint = { protocol: 'http', name: 'getUsers' };
    console.log("asdasd",weakMap.has(endpoint))
    queryAPI(endpoint);
    console.log("asdasd",weakMap.has(endpoint))
    console.log("asdasd",weakMap.get(endpoint))
    queryAPI(endpoint);
    console.log("asdasd",weakMap.get(endpoint))
    queryAPI(endpoint);
    queryAPI(endpoint);
    console.log("asdasd",weakMap.get(endpoint))