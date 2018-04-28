<template>


<iframe style="width:800px;height:580px" :src="src">
  
</iframe>

</template>
<script>
  export default {
    data() {
      return {
        activeName: 'second',
        channel:1025,
        src:""
      };
    },
    created(){
        this.src = "https://wb.agora.io/html/agora-wb.html?key=dab77282fe784dc085c411ee19f34422&cname="+this.channel+"&role=host"
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
      },

    },

  };
</script>