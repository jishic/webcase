<template>
    <div>
        <div class="head">
            <img  class="shape shape1" src="../assets/head.jpg">
            <div class="middle">
                <b><p >{{title}}</p></b>
                <span ><i class="el-icon-view fire"></i> {{watchs}}</span>
            </div>
            <div class="right">
                <div class="attention_sty ">{{attention}}</div>
                <div class="attention_sty attention_sty_btn" @click="logins"><i class="el-icon-star-off "></i>  关注</div>
                
            </div>
        </div>
        <div class="mainbody">
            <transition>
                <el-tabs type="border-card">
                    <el-tab-pane label="PPT" >
                        <ppt></ppt>
                    </el-tab-pane>
                    <el-tab-pane label="Editor" >       
                        <editor/>
                    </el-tab-pane>
                    
                    <el-tab-pane>
                        <span slot="label"><i class="el-icon-picture-outline"></i> 白板</span>
                        <div class="cont"><whiteboard/></div>
                    </el-tab-pane>
                    
                </el-tabs>
            </transition>
            <transition>
                <el-collapse-transition>
                    <div>
                        <div class="teacher"><camera/></div>
                        <div class="chat">
                            <chatroom />
                        </div>
      
                    </div>
                </el-collapse-transition>
            </transition>
        </div>
    </div>
</template>




<script>
import "element-ui/lib/theme-chalk/index.css";
import "vue/dist/vue.js";
import chatroom from "./student_chatroom";
import camera from './video_student'
import whiteboard from './whiteboard_student';
import editor from './editor_student';
import ppt from './ppt_student'
export default {
  components: {
    editor,
    chatroom,
    camera,
    whiteboard,
    ppt
    },
  data() {
    return {
      title:"左右征战，大杀四方",
      watchs:325,
      attention:3250,
      username:"刘德华",
      goEasy:"",
      input_message:"",

    };
  },
    methods: {
  }
}

</script>

<style scoped>
#studio{
    width:100%;
    height: 900px;
    padding-top: 60px;
    background: #F5F5F5;
}
.head{

    width:830px;
    height: 100px;
    margin-left: 350px;
    margin-top: 20px;
    
}

.shape{
    float: left;
    width: 90px;
    height: 90px;
    -moz-border-radius: 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px;
}
.shape1{
    margin-left:5px;
    margin-top: 5px
}
.middle{
    float: left;
    margin-left: 30px;
    color: rgb(39, 74, 89);
}
.watch_sty{
    font-size: 10px;
    margin-top: 100px;
}
.middle p{
    font-size: 25px;
    margin-bottom: 15px;
    margin-top: 15px;
}
.fire{
    color: rgb(8, 191, 145);
    margin-left: 50px;
}
.right{
    float: right;
    margin-right: 20px;
    margin-top: 20px;
}
.middle span{
    margin-left: 0px;
}
.mainbody {
  display: flex;
  margin-top: 20px;
  height:780px;
}
.attention_sty{
    border:1px solid rgb(229,229,229);
    float: right;
    height: 35px;
    width: 80px;;
    text-align: center;
    padding-top: 12px; 
    background: white;
    color: rgb(39,40,34)
}
.attention_sty_btn{
    background: rgb(26, 209, 163);
    color: white;
}
.attention_sty_btn:hover{
    cursor: pointer;
}
.el-tabs {
  margin-left: 350px;
  width: 830px;
  height: 670px;
}
.cont {
  width: 800px;
  height: 600px;
}
.right {
  background: #909399;
}
.teacher {
  margin-bottom: 12px;
  width: 300px;
  height: 200px;
  border-radius: 4px;
  background-color: #909399;
  text-align: center;
  color: #fff;
  box-sizing: border-box;
  margin-right: 20px;

}
.chat {
  width: 300px;
  height: 320px;
  border-radius: 4px;

  box-sizing: border-box;
  margin-right: 20px;  
}
.el-input {
  width: 223px;
}
.font_sty{
    font-size: 13px;
    color:rgb(136,136,136);
    margin-left: 6px;

}
.tea_sty{
    color:rgb(8, 191, 145);
    
}
.stu_sty{
    color:rgb(199,37,78);
}
</style>