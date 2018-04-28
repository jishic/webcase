<template>

<div class="all">
    
    <div class="chat_room_panel " >
        <div id="area">
        </div>
    </div>
    <div class="input_sty">
    <input placeholder="请输入内容" id="input_texts" type="text" v-model="input_text"></input>
    <button type="success"  @click="sentMessage" class="btn">Publish</button>
    </div>         
</div>
</template>
 
<script>



export default {

    data(){
        return {
            goEasy:"",
            input_message:"",
            username:"",
            imgURL:"../../static/icon.jpg"
        }
    },
    created () {
        this.goEasy = new GoEasy({appkey: 'BC-89e5ba0fe2264fa0b5994b94557e4a08'})
        this.username = sessionStorage.getItem('username').split('"')[1]
    },
    methods:{
        sentMessage:function(){
            var myDate = new Date();//获取系统当前时间

            this.goEasy.publish({
                channel:'102596',
                message:'<div class="all_content"><p>'+myDate.toLocaleString()+'</p><img src="'+this.imgURL+'" class="shape"><div class="content"><div class="content_word_stu">'+this.input_text+'</div></div></div>'
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
.all{
    height:460px;
    width:300px;
    background: rgb(255,255,255);
    
}
#area{
    height: 415px;
    width:300px;
    background: rgb(255,255,255);
    border-bottom: 1px solid rgb(228,228,232);
 
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
#input_texts{
    margin-left: 15px;

    height:30px;
    background:rgb(236,236,239);
    width: 180px;
    font-size: 15px;
    padding-left:5px; 
    border:none
}
.btn{
    width: 80px;
    height: 30px;
    background: rgb(26, 209, 163);
    border:none;
    color: white;
    margin-left: 5px;
}
.btn:hover{
    background: rgb(8, 191, 145);
}
.input_sty{
    margin-top: 10px;
}
.shape{
    float: left;
    width: 30px;
    height: 30px;
    background: red;
    -moz-border-radius: 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px;
}

.all_content{
    margin-left: 10px;
}
.all_content p{
    color: rgb(179,152,183);
    font-size: 10px;
    margin-left: 40px;
    margin-bottom: 3px;
}
.all_content{
    height: 60px;
}
.content_word_stu{
    float: left;
    margin-left: 10px;
    margin-top: 2px;
    text-align: center;
    height: 30px;
    background: rgb(236,236,239);
    padding-left: 10px;
    padding-right: 10px;
    line-height: 30px;
    color:rgb(71,72,101);
    font-size: 15px;
}

.content_word_tea{
    float: left;
    font-size: 15px;
    margin-left: 10px;
    margin-top: 2px;
    text-align: center;
    height: 30px;
    background: rgb(8, 191, 145);
    padding-left: 5px;
    padding-right: 10px;
    line-height: 30px;
    color:white;
}
</style>