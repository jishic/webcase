<template>
<div>
<div id="navigation">
<br>
    <div id="title">
    <img id ="img" src="../assets/logo.png">
    <div id="text">
    <span class="font">{{ msg }}</span>
    <span class="font2">{{ msg2 }}</span>
    </div>
    <div id ="login" v-if="!login_seen" >
        <el-dropdown>
        <i class="el-icon-star-off star" @mouseover="showList"></i>  
        <el-dropdown-menu slot="dropdown" class="show_List">
        <span v-for="n in atlist">
            <el-dropdown-item v-if="n.type==true">
                <p class="show_List_p1" >{{n.name}}的直播间~</p>
                <p class="show_List_p2" >主播名:{{n.name}} <span class="show_List_span">● 直播中</span></p>
            </el-dropdown-item>
            <el-dropdown-item v-if="n.type==false" disabled>
                <p class="show_List_p1" >{{n.name}}的直播间~</p>
                <p class="show_List_p2" >主播名:{{n.name}} <span class="show_List_span2">● 未开播</span></p>
            </el-dropdown-item>
        </span>
        </el-dropdown-menu>
        </el-dropdown>

    
        <el-dropdown>
        <el-button type="primary"  class="shape">
            <img :src="head"  class="shape shape1">
        </el-button>
        <el-dropdown-menu slot="dropdown" >
            <el-dropdown-item @click.native = "move1">个人中心</el-dropdown-item>
            <el-dropdown-item @click.native = "move2">密码修改</el-dropdown-item>
            <el-dropdown-item @click.native = "move3">我的关注</el-dropdown-item>
            <el-dropdown-item v-if="isTea" @click.native = "move4">开启直播</el-dropdown-item>
            <el-dropdown-item @click.native="logout">注销登录</el-dropdown-item>
        </el-dropdown-menu>
        </el-dropdown>
      
    </div>
    <div id="login" v-if="login_seen"> 
        <button class="but_sty" @click="logins" >登录</button>
        <button class="but_sty but_zhu"  @click="registers">注册</button>
        <el-dialog :visible.sync="visible" class="login_dialog">
        <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="登录" name="first">
            <div> 
               <el-form :model="LoginForm" status-icon ref="LoginForm" :rules="rules" >
                <br>
                    <el-form-item prop="username">
                    <el-input type="text" v-model="LoginForm.username" placeholder="请输入用户名"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                    <el-input type="password" v-model="LoginForm.password" placeholder="请输入密码"></el-input>
                    </el-form-item>
                    <el-form-item prop="identify">
                    <el-input type="text"  class="confirm-input"  v-model="LoginForm.identify" placeholder="验证码" ></el-input>
                    <img class="confirm" src="../assets/confirm.png">
                    </el-form-item>
    
                <a  class="forget_pass" @click="forgetPass">忘记密码？</a>  
                <br>
               
                    <el-button type="primary" class="submimts" @click="login_methods">登录</el-button>
            </el-form>  
            </div>

        </el-tab-pane>
        <el-tab-pane label="注册" name="second">
            <div>
            <el-form :model="RegisterForm" status-icon ref="RegisterForm" :rules="rules2" >
               
                    <el-form-item prop="username">
                    <el-input type="text" v-model="RegisterForm.username"  placeholder="请输入用户名"></el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                    <el-input type="password" v-model="RegisterForm.password" placeholder="请输入密码"></el-input>
                    </el-form-item>
                    <el-form-item prop="telphone">
                    <el-input type="text" v-model="RegisterForm.telphone" placeholder="请输入电话"></el-input>
                    </el-form-item>
                    <div class="container">
                        <el-form-item prop="identify_tel">
                        <el-input type="text" v-model="RegisterForm.identify_tel" placeholder="请输验证码"/><br>
                        <button class="require" @click="requireTel" >{{tel_message}}</button>
                    </el-form-item>
                    </div>
                    <el-button  class="submimts" @click="register_methods">注册</el-button>
            </el-form>  
            </div>
        </el-tab-pane>
        </el-tabs>
        </el-dialog>
    </div>
    </div>
    <div id="meau">
    <ul>
        <li><button class="meau_btn meau_main"><i class="el-icon-menu" ></i>  首页</button></li>
        <li><button class="meau_btn" @click="movie">直播</button></li>
        <li><button class="meau_btn">录播</button></li>
    </ul>
    <div class="search bar7">
        <form>
            <input type="text" placeholder="  请输入..." maxlength="7">
            <a><i class="el-icon-search" ></i></a>
        </form>
    </div>
    </div>
</div>
<div class="choose_box" v-if="choose_box_seen">  
    <table class="choose_box_table">
    <tr>
        <td><div  class="choose_box_tr"><span class="choose_box_table_span">后端开发</span><span class="smaller">Python PHP</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr"><span class="choose_box_table_span">Linux运维</span><span class="smaller"> Linux Shell</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr"><span class="choose_box_table_span">云计算与大数据</span><span class="smaller"> Hadoop Spark</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr"><span class="choose_box_table_span">数据库</span><span class="smaller"> SQL NoSQL</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr"><span class="choose_box_table_span">信息安全</span><span class="smaller"> Web安全 安全开发</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr"><span class="choose_box_table_span">Web前端</span><span class="smaller"> HTML5 Web</span></div></td>
    </tr>
    <tr>
        <td><div class="choose_box_tr1"><el-button type="primary" class="choose_box_btn " size="mini" round>经管专区</el-button><el-button type="primary" class="choose_box_btn" size="mini" round>软件库</el-button></div></td>
    </tr>
  
    </table>
    </div>


</div>
</template>

<script>
import 'element-ui/lib/theme-chalk/index.css'
import axios from '../api/axios'
import getUrl from '../api/getPath'

export default {
  data () {
    var validateIden = (rule, value, callback) => {    
        value=value.toLowerCase()
        if (value === '') {
            callback(new Error('请输入验证码'));
        } else if (value!==("giv6j")) {
            callback(new Error('验证码不正确!'));
        } else {
            callback();
    }
    };
    var validateTel = (rule, value, callback) => {    
        var re = /^1\d{10}$/
        if (value === '') {
            callback(new Error('请输入电话'));
        } else if (!re.test(value)) {
            callback(new Error('电话号码格式不正确!'));
        } else {
            callback();
        }
    };
    var validateIdenByTel = (rule, value, callback) => {    
        if (value === '') {
            callback(new Error('请输入验证码'));
        } else if (value!==this.my_identify_tel) {
            callback(new Error('验证码不正确!'));
        } else {
            callback();
        }
    };
    return {
      
        msg: '双子楼',
        msg2: ' ',
        visible:false,
        login_seen:true,
        activeName:'first',
        choose_box_seen:false,
        isTea:false,
        my_identify_tel:"",
        atlist:[],
        tel_message:"获取验证码",
        LoginForm:{
            password: "",
            username: "",
            identify: ""
        },
        RegisterForm:{
            password: "",
            username: "",
            telphone:"",
            identify_tel: ""
        },
        head:"",
        username:"",
        rules: {
            username: [{
            required: true,
            message: "请输入用户名",
            trigger: 'blur'
            }],
            password: [{
            required: true,
            message: "请输入密码",
            trigger: 'blur'
            }],
            identify: [{
            required: true,
            validator: validateIden,//验证码验证
            trigger: 'blur'
            }]
        },
        rules2:{
            username: [{
            required: true,
            message: "请输入用户名",
            trigger: 'blur'
            }],
            password: [{
            required: true,
            message: "请输入密码",
            trigger: 'blur'
            }],
            telphone: [{
            required: true,
            validator: validateTel,
            trigger: 'blur'
            }],
            identify_tel: [{
            required: true,
            validator: validateIdenByTel,//电话验证
            trigger: 'blur'
            }],
        
        },
      
    }

  },
  methods:{
    registers: function () {
        this.visible = true
        this.activeName='second'
            
    },
    logins: function(){
        this.visible = true
        this.activeName='first'
      
    },
    forgetPass:function(){
        this.visible=false
        this.choose_box_seen=false
        this.$router.push({
            path: '/forgetPass',
            params: { 
            }
        })
    },
    login_methods: function(e){
        this.$refs.LoginForm.validate((valid) => {
            if (valid) {
                const url = getUrl('backend/login')//127.0.0.1
                //const url = '/backend/login'//127.0.0.1
                var params = new URLSearchParams()
                params.append('username', this.LoginForm.username)
                params.append('password', this.LoginForm.password)  
                this.$axios({
                method: 'post',
                url: url,
                data: params  //get params     post data
                }).then((res) => {
                if(res.data.success ){
                    this.visible = false
                    this.login_seen=false
                    
                    this.choose_box_seen=true
                    this.isTea=res.data.isTea
                    this.$message.success('登录成功');
                    sessionStorage.setItem('username',res.data.username);
                    sessionStorage.setItem('email',res.data.email);
                    sessionStorage.setItem('gender',res.data.gender);
                    sessionStorage.setItem('telephone',res.data.telephone);
                    sessionStorage.setItem('isTea',res.data.isTea);
                    sessionStorage.setItem('imgpath',res.data.imgpath);
                    this.head=res.data.imgpath;
                    this.$router.push({
                        name: 'lifestreem',
                        params: { 
                        }
                    })
                }
                else{
                    this.$message.error('用户名或密码错误');
                }
                this.$refs.LoginForm.resetFields();
                })
            } 
            });
    },
    register_methods: function(e){
        this.$refs.RegisterForm.validate((valid) => {
            if (valid) {
                const url = getUrl('backend/regist')//127.0.0.1
                //const url = '/backend/register'//127.0.0.1
                var params = new URLSearchParams()
                params.append('username', this.RegisterForm.username)
                params.append('password', this.RegisterForm.password)  
                params.append('telphone',this.RegisterForm.telphone)
                params.append('src','/static/head.jpg')
                this.$axios({
                method: 'post',
                url: url,
                data: params  //get params     post data
                }).then((res) => {
                if(res.data.success){
                    this.visible = false
                    this.login_seen=false
                    this.head=res.data.imgUrl
                    this.$message.success('注册成功');
                    this.isTea=false
                    console.log(res.data)
                    sessionStorage.setItem('username',res.data.username);
                    sessionStorage.setItem('password',res.data.password);
                    sessionStorage.setItem('email', res.data.email);
                    sessionStorage.setItem('gender', res.data.gender);
                    sessionStorage.setItem('telephone', res.data.telephone);
                    sessionStorage.setItem('isTea', res.data.isTea);
                }
                else{
                    this.$message.error('用户名已存在');
                }
                this.$refs.RegisterForm.resetFields();
                })
            } 
            });
    },
    logout:function(){
        this.confirm_logout()
        this.username=""
        
    },
    confirm_logout:function(){
        this.$confirm('是否确定退出?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning',
        }).then(() => {
            this.login_seen=true
            this.visible = false
            this.choose_box_seen=true
            sessionStorage.setItem('username',"");
            sessionStorage.setItem('password',"");
            sessionStorage.setItem('email', "");
            sessionStorage.setItem('gender', "");
            sessionStorage.setItem('telephone', "");
            sessionStorage.setItem('isTea', "");
            this.$router.push({
                name: 'lifestreem',
                params: { 
            }
    
        })
        }).catch(() => {
        });
    },
    showList:function(){      
        const url = getUrl('backend/attention')
        //const url = '/backend/attention'
        var params = new URLSearchParams()
        params.append('username', sessionStorage.getItem('username'))
        // params.append('username', 'wwk')
        this.$axios({
                method: 'post',
                url: url,
                data: params  //get params     post data
            }).then((res) => {
                if(res.data.success){
                    this.atlist=res.data.list;
                }
                else{
                    this.$message.success('没有喜欢的主播哦，快去关注吧~');
                }
            })

    },
    requireTel:function(obj){

        if(this.RegisterForm.telphone!=""){
        var arr = [];//容器  
            for(var i =0;i<6;i++){//循环六次  
                var num = Math.random()*9;//Math.random();每次生成(0-1)之间的数;  
                num = parseInt(num,10);  
                arr.push(num);  
            } 
        this.my_identify_tel=arr.join("")
        const url = getUrl('backend/sendcode')
        //const url = '/backend/requireidentify'
        var params = new URLSearchParams()
        params.append('telphone', this.RegisterForm.telphone)
        params.append('identify', this.my_identify_tel)  
        console.log(this.my_identify_tel)
        this.$axios({
            method: 'post',
            url: url,
            data: params  //get params     post data
            }).then((res) => {
            if(!res.data.success){
                this.$message.error('电话号码错误');
            }
            else{
                this.$message.success('短信已发送，请注意查收');
            }
            })
        }
        else{
            this.$message.error('请输入电话号码');
        }
      
    },
    move1:function(){
        this.choose_box_seen=false;
		this.$router.push({
		name: 'PersonalDate',
		params: {
		    username: ''
		    }
		})
	},
	move2:function(){
        this.choose_box_seen=false;
		this.$router.push({
		name: 'ChangePassword',
		params: {
		username: ''
		}
		})
	},
    move3:function(){
        this.choose_box_seen=false;
        const url = getUrl('backend/attention');//127.0.0.1
        var params = new URLSearchParams();
        params.append('username',sessionStorage.getItem('username'));
        this.$axios({
            method: 'post',
            url: url,
            data: params  //get params     post data
        }).then((res) => {
            if(res.data.success ){
                sessionStorage.setItem('focuslist',JSON.stringify(res.data.list));
                this.$router.push({
                    name: 'FocusList',
                    params: { 
                    }

                })
            }
            else{
                this.$message.error('获取关注列表错误');
            }
        })
	},
    move4:function() {
        this.choose_box_seen=false;
        this.$router.push({
            name: 'ApplyLive',
            params: {
            }
        })

    },
    movie:function(){
        this.choose_box_seen=false;
    	this.$router.push({
    		name: 'student',
    		params: {
    		}
    	})
    }
    }
}

</script>

<style scoped>
#navigation{
    height:150px;
    width: 100%;
    margin-top: -8px;
    background: rgb(247, 247, 247);
    border-bottom: 2px solid rgb(200,200,200)
}
#title{
    margin-left: 380px; 
    margin-right: 400px; 
}
#img{
    float: left;
    height: 45px;
    width: 40px;

}
#text{
    float: left;
    margin-left: 5px;
    text-align: center;
}
.font{
    font-size: 30px;
    font-weight:bolder;
    
    color: rgb(39, 74, 89);
}
.font2{
    font-size: 20px;
    color: rgb(39, 74, 89);
    margin-left: 15px;
}
#login{
    float: right;
}
.but_sty{ 
    width: 82px;
    height: 43px;
    border:0px;
    background: rgb(247, 247, 247);
    color: rgb(39, 74, 89);
    font-size: 18px;
    

}
.but_zhu{
    background: rgb(8, 191, 145);
    color:rgb(247, 247, 247);
}
.but_sty:hover{
    background: rgb(238, 238, 238);
}
.but_zhu:hover{
    background: rgb(26, 209, 163);
}
.el-dialog{
    height: 450px;
    width: 150px; 
}

.submimts{
    width: 310px;
    height: 40px;
    background: rgb(64, 158, 255);
    color:white;
    border:0px;
    margin-top: 20px;
    font-size: 18px;
  
}
.confirm-input{
    float: left;
    width:140px;
}
.confirm{
    float: left;
    margin-left: 20px;
    width :130px;
    height :40px;
}
 .container{
    position:relative;
}
.require{
    position:absolute;
    width:90px;
    height:40px;
    top:0px;
    right:0px;
    z-index:99;
    border:0px;
    background: rgb(64, 158, 255);
    color:white;
    font-weight: bolder;
    
}

.shape{
    float: right;
    width: 50px;
    height: 50px;
    background: red;
    -moz-border-radius: 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px;
}
.shape1{
    margin-right:-21px;
    margin-top: -14px
}
.star{
    float: left;
    font-size:25px;
    margin-top:-30px;
    margin-right:20px;
}
.star:hover{
    color:rgb(26, 209, 163);
}
#meau{
    background: white;
    height: 49px;
    margin-top: 80px;
    margin-left: 350px; 
    margin-right: 400px; 
}
#meau li{
    float: left;
    list-style: none;
}
.meau_btn{
    border:0px;
    color: rgb(39, 74, 89);
    height: 49px;
    font-size: 20px;
    width: 80px;
    background: white
}
.meau_main{
    background: rgb(8, 191, 145);
    width: 250px;
    color: white;
    margin-left: -40px;
}
.meau_btn:hover{
    color: rgb(8, 191, 145);
}
.meau_main:hover{
    color: white;
    background: rgb(26, 209, 163);
}

.bar7 input {
    padding-left:15px;
    width: 140px;
    border-radius: 42px;
    height: 25px;
    border: 2px solid #324B4E;
    background: white;
    transition: .3s linear;
    z-index:0;
    margin-top: 10px;
    float: right;
    font-size:15px;
    outline: none;
}
.bar7 input:focus {
    width: 160px;

}
.bar7 a{
    z-index:2;
    position:absolute;
    margin-left: 700px;
    margin-top: 15px
}
.login_dialog{
    width:670px;
    margin-left: 30%;
}
.choose_box{
    position:absolute;
    z-index:5;
    width: 250px;
    background: rgba(72,81,83, 0.5);
    height: 520px;
    margin-left:350px;
 
}
.choose_box_tr{
    height:71px;
    width: 250px;
    color: white;
    margin-left: -1px;
    font-size:16px;
    display:flex;/*Flex布局*/
    display: -webkit-flex; /* Safari */
    align-items:center;/*指定垂直居中*/
 
}
.smaller{
    font-size:5px;
    margin-left: 10px;
}
.choose_box_tr:hover{
    background: white;
    color: rgb(39, 74, 89);
    cursor: pointer;
}
.choose_box_tr1{
    border-top: 0.5px solid white;
    height:71px;
    width: 250px;
    margin-left: 0px;
    font-size:16px;
    display:flex;/*Flex布局*/
    display: -webkit-flex; /* Safari */
    align-items:center;/*指定垂直居中*/
  
}
.choose_box_btn{
    background: rgba(72,81,83, 0.7);
    color: white;
    border-color:white; 
    margin-left: 30px;
}
.choose_box_btn:hover{
    background: white;
    color: rgb(39, 74, 89);
}
button,el-button:hover{
    cursor: pointer;
}
.show_List{
    width:240px;
}
.show_List_p1{
    font-size:18px;
}
.show_List_p2{
    margin-top:-20px;
}
.show_List_span{
    color:rgb(26, 209, 163);
    float:right;
}
.show_List_span2{
    color:red;
    float:right;
}
.forget_pass{
    float:right;
    color:rgb(153, 153, 153);
    text-decoration:none;
}
.forget_pass:hover{
    cursor: pointer;
}
.register_input{
    margin-top:15px;
}
.choose_box_table{
    margin-top:-3px;
    border-collapse:separate; 
    border-spacing:0px;
}
.choose_box_table_span{
    margin-left: 20px;
}
</style>
