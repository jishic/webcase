<template>
    <el-container>
        <el-aside>
     	    <el-row class="tac">
                <el-col :span="20">
                    <el-menu default-active="2" class="el-menu-vertical-demo">
                        <el-menu-item index="1" @click = "move1">
                            <i class="el-icon-edit"></i>
                            <span slot="title">个人资料</span>
                        </el-menu-item>
                        <el-menu-item index="2" @click = "move2">
                            <i class="el-icon-setting"></i>
                            <span slot="title">密码修改</span>
                        </el-menu-item>
                        <el-menu-item index="3" @click = "move3">
                            <i class="el-icon-menu"></i>
                            <span slot="title">关注列表</span>
                        </el-menu-item>
                        <el-menu-item index="4" @click = "move4" v-if="istea">
                            <i class="el-icon-bell"></i>
                            <span slot="title">申请直播间</span>
                        </el-menu-item>
                    </el-menu>
                </el-col>
            </el-row> 
  	    </el-aside>
        <el-main>
            <el-form ref="changePassForm" :model="changePassForm" label-width="100px" :rules="rules">
                <el-form-item label="旧密码" prop="oldp">
                    <el-input v-model="changePassForm.oldp" type="password"></el-input>
                </el-form-item>
                <el-form-item label="新密码" prop="newp1">
                    <el-input v-model="changePassForm.newp1" type="password"></el-input>
                </el-form-item>
                    <el-form-item label="确认新密码" prop="newp2">
                    <el-input v-model="changePassForm.newp2" type="password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="changePass_method">确认修改</el-button>
                    <el-button @click="reset_method">重置</el-button>
                </el-form-item>
            </el-form>
        </el-main>
    </el-container>
</template>
<style scoped>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
    margin-left: 400px;
    width: 200px;
  }
  .el-main {
  	margin-left: 200px;
    margin-top: 100px;
  }
  .el-input {
  	width: 300px;
  }

</style>

<script>
	import 'element-ui/lib/theme-chalk/index.css';
	import 'vue/dist/vue.js'
	import axios from '../api/axios'
	import getUrl from '../api/getPath'
    export default {
  	    data() {
			var validatePass = (rule, value, callback) => {    
				value=value.toLowerCase()
				if (value === '') {
					callback(new Error('请输入原始密码'));
				}else {
					callback();
				}
			};
			var validateNewP1 = (rule, value, callback) => {    
				value=value.toLowerCase()
				if (value === '') {
					callback(new Error('请输入新密码'));
				}else {
					callback();
				}
			};
			var validateNewP2 = (rule, value, callback) => {    
				value=value.toLowerCase()
				if (value === '') {
					callback(new Error('请确认新密码'));
				}else {
					callback();
				}
			};
			return {
				changePassForm: {
					oldp: '',
					newp1: '',
					newp2: '',
                    istea: '',
				},
				rules: {
					oldp: [{
						required: true,
						validator: validatePass,
						trigger: 'blur'
					}],
					newp1: [{
						required: true,
						validator: validateNewP1,
						trigger: 'blur'
					}],
					newp2: [{
						required: true,
						validator: validateNewP2,
						trigger: 'blur'
					}],
				}
			};
        },
        created() {
            var istea = sessionStorage.getItem('isTea');
            if(istea === "false") {
                this.istea = false;
            }else {
                this.istea = true;
            }
        },
  	    methods: {
            move1:function(){
                this.$router.push({
                    name: 'PersonalDate',
                    params: {
                        username: ''
                    }
                })
            },
            move2:function(){
                this.$router.push({
                    name: 'ChangePassword',
                    params: {
                        username: ''
                    }
                })
            },
            move3:function(){
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
                this.$router.push({
                    name: 'ApplyLive',
                    params: {
                        username: ''
                    }                    
                })
            },
            changePass_method:function(e) {
				if(this.changePassForm.newp1 === this.changePassForm.newp2){
					this.$refs.changePassForm.validate((valid) =>{
						if(valid) {
							const url = getUrl('backend/changepassword') //后台的URL
							var params = new URLSearchParams()
							var username = sessionStorage.getItem('username')
							params.append('username',username);
							params.append('password', this.changePassForm.oldp);
							params.append('newpassword', this.changePassForm.newp1);
							this.$axios({
								method: 'post',
								url: url,
								data: params
							}).then((res) => {
								if(res.data.success) {
									sessionStorage.setItem('password',this.changePassForm.newp1);
									this.$message.success('密码修改成功');
								}
								else {
									this.$message.error('密码修改失败');
								}
								this.$refs.changePassForm.resetFileds();
							})
						}
					})				
				}else {
					this.$message.error('两次输入的新密码不相同');
				}
            },
            reset_method:function() {
                this.changePassForm.oldp = '';
                this.changePassForm.newp1 = '';
                this.changePassForm.newp2 = '';
            }
        }
    }
</script>