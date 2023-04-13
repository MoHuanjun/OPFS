<template>
  <body id="poster">
    <el-form :rules="loginRules" ref="loginRules" :model="loginData" class="login_container" label-position="left" label-width="0px">
      <h1  class="login_title">{{ titleMsg }}</h1>
      <el-form-item prop="username" :rules="[{required: true, message: '用户名不能为空'}]">
        <el-input ref="username" type="username" v-model="loginData.username" placeholder="用户名" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item prop="password" :rules="[{required: true, message: '密码不能为空'}]">
        <el-input type="password"  v-model="loginData.password" placeholder="密码" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width:100% ; background : #B4EDF8 ; border: none" v-on:click="loginForm()">登录</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" style="width:100% ; background : #ABD1EF ; border: none" v-on:click="toRegister()">注册</el-button>
      </el-form-item>
    </el-form>
  </body>
</template>
<script>
import qs from 'qs'
import service from '@/utils/request'

export default {
  name: 'loginForm',
  data() {
    return {
      titleMsg: '欢迎使用',
      loginData: {
        username: '',
        password: ''
      },
      loginRules: {
        username: [{
          required: true,
          message: "请输入用户名",
          trigger: "blur"
        },
          {
            min: 3,
            max: 18,
            message: "长度在 3 到 18 个字符",
            trigger: "blur",
          },
        ],
        password: [{
          required: true,
          message: "请输入密码",
          trigger: "blur"
        },
          {
            min: 3,
            max: 18,
            message: "长度在 3 到 18 个字符",
            trigger: "blur",
          }
        ]
      }
    }
  },
  methods: {
    loginForm() {
      this.$refs.loginRules.validate((valid) => {
        if (valid) {
          service({
            url: '/login',
            method: 'post',
            data: qs.stringify(this.loginData)
          }).then(response => {
            if (response.data.code === 200) {
              this.$message({
                message: '登录成功',
                type: 'success'
              })
              this.$router.push({path: '/uploader'})
            } else {
              this.$message({
                message: '登录失败',
                type: 'error'
              })
            }
          })
        } else {
          this.$message({
            message: '请检查输入',
            type: 'error'
          })
        }
      })
    },
    toRegister(){
      this.$router.push({path:'/register'})
    },
  }
}
</script>

<style>
#poster{
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed
}
body{
  margin: 0;
  padding:0
}
.login_container{
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.login_title{
  margin: 0 auto 40px auto;
  text-align: center;
  color: #505458
}
</style>
