import axios from 'axios'
import Cookies from 'js-cookie'


/****** 创建axios实例 ******/
const service = axios.create({
    baseURL: 'http://localhost:5000',  // api的base_url
    timeout: 5000  // 请求超时时间
})

service.interceptors.request.use(
    config => {
        config.headers['Authorization'] = Cookies.get('Authorization')
        return config
    },
    error => {
        console.log(error)
        return Promise.reject(error)
    }
)

/****** response拦截器==>对响应做处理 ******/
service.interceptors.response.use(
    response => {
        const { data } = response
        if (isJSON(data.data)) {
            let jsonObj = JSON.parse(JSON.stringify(data.data))
            if (Object.prototype.hasOwnProperty.call(jsonObj,"token")){
                console.log('update token')
                Cookies.set('Authorization',jsonObj.token)
            }
        } else {
            console.log('not')
        }
        return response
    },
    error => {
        console.log(error);
        return Promise.reject(error)
    }
)

function isJSON(str) {
    let jsonData = JSON.stringify(str)
    try {
        if (typeof JSON.parse(jsonData) == "object") {
            return true;
        } else {
            return false;
        }
    }
    catch(e) {
        return false;
    }
}

export default service;

