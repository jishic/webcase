<template>
  <div id="app">
    <my-head></my-head>
 
    <router-view/>

    <foot ></foot>
  </div>
</template>

<script>
import myHead from "./components/Top.vue"
import foot from "./components/foot.vue"
export default {
  
  data:function(){
    return{
      name: 'App',
    }
  },
  components:{
    "my-head":myHead,
    "foot":foot
  },
}

</script>
<style>
#app{
  width: 100%;
}

</style>



