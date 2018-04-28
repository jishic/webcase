<template>

<div class="forgerpass">
    <div class="whiteB">
        <div class="pass_top">
        <i class="el-icon-goods"></i>找回密码
        </div>
        <div class="pass_step">
        <el-steps :active="active" finish-status="success">
        <el-step title="填写手机号"></el-step>
        <el-step title="验证身份"></el-step>
        <el-step title="设置新密码"></el-step>
        <el-step title="完成"></el-step>
        </el-steps>
        </div>
        <div class="content">
        <div v-if="activeName === '1'">
            <!-- 手机号输入<el-button style="margin-top: 12px;" @click="next1">下一步</el-button> -->
           <el-form :model="Telphones" :rules="rule1" ref="Telphones" label-width="100px" >
            <el-form-item label="电话号码" prop="telphone">
                <el-input v-model="Telphones.telphone" class="input_sty"></el-input>
            </el-form-item>
            <el-button type="success" round class="button_fir" @click="next1">下一步</el-button>
            </el-form>
        </div>
        <div v-if="activeName === '2'">
            <el-form :model="Identify" :rules="rule2" ref="Identify" label-width="100px" >
            <el-form-item label="验证码" prop="identify_tel">
                <el-input v-model="Identify.identify_tel" class="input_sty"></el-input>
            </el-form-item>
            <el-button type="success" round class="button_fir" @click="next2">下一步</el-button>
            </el-form>
        </div>
        <div v-if="activeName === '3'">
            <el-form :model="NewPass" :rules="rule3" ref="NewPass" label-width="100px" >
            <el-form-item label="新密码" prop="newpass">
                <el-input type="password" v-model="NewPass.newpass" class="input_sty"></el-input>
            </el-form-item>
            <el-button type="success" round class="button_fir" @click="next3">下一步</el-button>
            </el-form>
        </div>
        <div v-if="activeName === '4'" class="success">
            修改密码成功！
        </div>

        
        </div>
  
    </div>
    
</div>

</template>

<script>
import 'element-ui/lib/theme-chalk/index.css'
import axios from '../api/axios'
import getUrl from '../api/getPath'
export default{
	data(){
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
            active: 1,
            activeName:"1",
            my_identify_tel:"",
            Telphones:{
                telphone:""
            },
            Identify:{
                identify_tel:""
            },
            NewPass:{
                newpass:""
            },
            rule1:{
                telphone:[{
                    required: true,
                    validator: validateTel,
                    trigger: 'blur'
                }]
            },
            rule2:{
                identify_tel:[{
                    required: true,
                    validator: validateIdenByTel,
                    trigger: 'blur'
                }]
            },
            rule3:{
                newpass: [{
                    required: true,
                    message: "请输入密码",
                    trigger: 'blur'
                    }],
            }
		}
	},
    methods :{
        next: function(){
        if (this.active++ > 3) this.active = 0;
        },
        next1: function(){
            this.requireTel()
        },
        next2: function(){
            this.$refs.Identify.validate((valid) => {
                if(valid){
                    this.activeName="3";
                    this.next();
                }
            })
        },
        next3: function(){
        
            this.$refs.NewPass.validate((valid) => {
                if(valid){
                    const url = getUrl('backend/forgetpassword')
                    //const url = '/backend/alterPass'//127.0.0.1
                    var params = new URLSearchParams()
                    params.append('newpass', this.NewPass.newpass)  
                    params.append('telphone', this.Telphones.telphone) 
                    this.$axios({
                            method: 'post',
                            url: url,
                            data: params  //get params     post data
                            }).then((res) => {
                            if(!res.data.success){
                                this.$message.error('修改密码失败');
                            }
                            else{
                                this.activeName="4";
                                this.next();
                                this.$message.success('修改成功');
                            }
                            })
                }
            })
        },
        next4: function(){
            
        },
        requireTel:function(obj){
            this.$refs.Telphones.validate((valid) => {
                if(valid){
                    //const url = getUrl('backend/alterPass')
                    if(this.Telphones.telphone!=""){
                    var arr = [];//容器  
                        for(var i =0;i<6;i++){//循环六次  
                            var num = Math.random()*9;//Math.random();每次生成(0-1)之间的数;  
                            num = parseInt(num,10);  
                            arr.push(num);  
                        } 
                    this.my_identify_tel=arr.join("")
                    const url = getUrl('backend/sendcodefp')
                    //const url = '/backend/requirePass'
                    var params = new URLSearchParams()
                    params.append('telphone', this.Telphones.telphone)  
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
                                this.activeName="2";
                                this.next();
                                this.$message.success('短信已发送，请注意查收');
                            }
                            })
                    }
                }
            })

            
            // else{
            //     this.$message.error('请输入电话号码');
            // }
            
            },

    }
}
</script>

<style scoped>
.forgerpass{
    height: 800px;
    background: rgb(242,242,242);
    padding-top:40px; 
    padding-left: 500px;
}
.whiteB{
    
    background: white;
    width: 910px;
    height: 550px;
    padding-top: 5px;
}
.pass_top{
    font-size: 30px;
    padding-left: 20px;
    padding-bottom: 15px;
    margin-top: 10px;
    border-bottom: 2px solid rgb(242,242,242);
}
.pass_step{
    width: 700px;
    margin-top: 40px;
    padding-left: 100px;
}
.content{
   padding-left: 240px;
   padding-top:60px;
}
.input_sty{
    width: 200px;
}
.button_fir{
    background: rgb(8, 191, 145);
    margin-left: 150px;
    margin-top: 50px;
}
.success{
    font-size: 30px;
    margin-left: 60px;
}
</style>