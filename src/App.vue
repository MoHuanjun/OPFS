<template>
  <div class='app'>
    <router-view></router-view>
  </div>
</template>


<script>
import Login from "./components/Login.vue";

export default{
  name: "LogIn",
  data(){
    return {};
  },
  components: {
    "app-user": Login,
  },
  methods: {}
}
</script>
