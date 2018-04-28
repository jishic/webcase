<template>

<div>
    <div class="chat_room_panel " >
        <div id="area">
        </div>
    </div>
    <div>
    <el-input placeholder="请输入内容" id="input_texts" type="text" v-model="input_text"></el-input>
    <el-button type="success" plain  @click="sentMessage" class="btn">发送</el-button>
    </div>         
</div>
</template>
 
<script>



export default {

    data(){
        return {
            goEasy:"",
            input_message:"",
            username:"晏宸",
        }
    },
    created () {
        this.goEasy = new GoEasy({appkey: 'BC-89e5ba0fe2264fa0b5994b94557e4a08'})
    },
    methods:{
        sentMessage:function(){
            this.goEasy.publish({
                channel:'102596',
                message:"<b><p class='font_sty'><span class='stu_sty'>"+this.username+"同学</span> : "+this.input_text+"</p></b>"
                });
            document.getElementById("input_texts").value=""
        },
        collect(){
            this.goEasy.subscribe({
                channel:'102596',
                onMessage(message){
    
                    document.getElementById("area").innerHTML+=(message.content)
                }
                });
        },
        blacklsit(){
            alert()
        },
        
        
    },
    mounted () {
        this.collect()
    }
}
</script> 
<style >
.chat_room_panel{
    height:300px;
    width:200px;
    background: rgb(241,241,241);
    border: 1px solid  rgb(8, 191, 145)
}
.font_sty{
    font-size: 13px;
    color:rgb(51, 51, 51);
    margin-left: 6px;
}
.tea_sty{
    color:rgb(8, 191, 145);
}
.stu_sty{
    color:rgb(199,37,78);
}
</style>