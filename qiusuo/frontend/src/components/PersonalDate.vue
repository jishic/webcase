<template>
  	<el-container>
        <el-aside>
     	    <el-row class="tac">
        		<el-col :span="20">
            		<el-menu default-active="1" class="el-menu-vertical-demo">
                		<el-menu-item index="1" @click = "move1">
                    		<i class="el-icon-edit"></i>
                    		<span slot="title">个人资料</span>
                		</el-menu-item>
                		<el-menu-item index="2" @click = "move2">
                    		<i class="el-icon-setting"></i>
                    		<span slot="title" >密码修改</span>
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
            <div class = "left">
                <el-input type="file" name="file" id="file_upload"></el-input>
        		<el-upload class="avatar-uploader">
      				<img v-if="imageUrl" :src="imageUrl" class="avatar">
      				<i v-else class="el-icon-plus avatar-uploader-icon"></i>
    			</el-upload>
                <el-button type="primary"  @click="FileUpload">上传</el-button>
            </div>
            <div class = "right">
    		    <el-form ref="DateForm" :model="DateForm" label-width = '100px' :rules = "rules">
    				<el-form-item label="用户名">
    				    <el-input v-model="DateForm.username" readonly></el-input>
    				</el-form-item>
    			    <el-form-item label="性别">
    				    <el-radio-group v-model="DateForm.sex">
      					    <el-radio label="男"></el-radio>
      					    <el-radio label="女"></el-radio>
    				    </el-radio-group>
    				</el-form-item>
    				<el-form-item label="邮箱">
    				    <el-input v-model="DateForm.email"></el-input>
    				</el-form-item>
                    <el-form-item label="电话号码">
                        <el-input v-model="DateForm.tel"></el-input>
                    </el-form-item>
    				    <el-form-item>
    				        <el-button type="primary" @click="changeDate_methods">修改资料</el-button>
    				        <el-button @click="reset_methods">重置</el-button>
    				    </el-form-item>
    		    </el-form>
            </div>
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
}
.el-input {
  	width: 300px;
}
.avatar-uploader {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    width: 180px;
    height: 180px;
}
.avatar-uploader:hover {
    border-color: #409EFF;
}
.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
}
.avatar {
    width: 178px;
    height: 178px;
    display: block;
}
.left {
    float:left;
}
.right {
    float:left;
}
</style>

<script>
	import 'element-ui/lib/theme-chalk/index.css';
	import 'vue/dist/vue.js'
	import axios from '../api/axios'
	import getUrl from '../api/getPath'


  	export default {
  	    data() {
            var validateEmail = (rule, value, callback) => {
                var res = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/
                if(value === '') {
                    callback();
                }else if(!res.test(value)) {
                    callback(new Error('请输入正确格式的邮箱地址'));
                }else {
                    callback();
                }
            };
            var validateTel = (rule, value, callback) => {
                var res = /^1\d{10}$/
                if(value === '') {
                    callback(new Error('请输入电话'));
                }else if(!res.test(value)) {
                    callback(new Error('请输入正确格式的电话号码'));
                }else {
                    callback();
                }
            };

      		return {
        		imageUrl: '',
                istea: '',
        		DateForm: {
					username: '',
        			sex: '',
        			email: '',
                    tel: ''
        		},
                rules: {
                    sex: [{
                        require: true,
                        trigger: 'blur'
                    }],
                    email: [{
                        require: true,
                        validator: validateEmail,
                        trigger: 'blur'
                    }],
                    tel: [{
                        require: true,
                        validator: validateTel,
                        trigger: 'blur'
                    }],
                }
      		};
    	},
		created() {
			var telstr = sessionStorage.getItem('telephone');
			this.DateForm.tel=telstr;
            var emailstr = sessionStorage.getItem('email');
            if(emailstr != "null") {
                this.DateForm.email=emailstr;
            }
			var genderstr = sessionStorage.getItem('gender')
			if(genderstr){
				this.DateForm.sex = "男";
			}else {
				this.DateForm.sex = "女";
			}
			var namestr = sessionStorage.getItem('username')
			this.DateForm.username=namestr;
            var istea = sessionStorage.getItem('isTea');
            if(istea === "false") {
                this.istea = false;
            }else {
                this.istea = true;
            }
            var imgpath = sessionStorage.getItem('imgpath');
            this.imageUrl = imgpath;           
		},
  	    methods: {
            FileUpload:function() {                  
                var form_data = new FormData();
                var file_info =$( '#file_upload')[0].files[0];
                form_data.append('image',file_info);
                form_data.append('username', this.DateForm.username);
                var url=getUrl('backend/fileupload');
                this.$axios({
                    method: 'post',
                    url: url,
                    data: form_data  //get params     post data
                }).then((res) => {
                    sessionStorage.setItem('imgpath',res.data.imgpath);
                    this.imageUrl = res.data.imgpath; 
                })
            },

      		move1:function() {
		        this.$router.push({
		        name: 'PersonalDate',
		        params: {
		          username: ''
		        }
		      })
		    },
		    move2:function() {
		        this.$router.push({
		        name: 'ChangePassword',
		        params: {
		          username: ''
		        }
		      })
		    },
          	move3:function() {
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
            changeDate_methods:function(e) {
                this.$refs.DateForm.validate((valid) =>{
                    if(valid) {
                        const url = getUrl('backend/changedata') //后台的URL
                        var params = new URLSearchParams()
						params.append('username', this.DateForm.username)
						if(this.DateForm.sex === "男")
						{
							params.append('gender', 1)
						}
						else {
							params.append('gender', 0)
						}
                        params.append('email', this.DateForm.email)
                        params.append('telephone', this.DateForm.tel)
                        this.$axios({
                            method: 'post',
                            url: url,
                            data: params
                        }).then((res) => {
                            if(res.data.success) {
                                this.$message.success('个人信息修改成功');
                            }
                            else {
                                this.$message.error('个人信息修改失败');
                            }
                            this.$refs.DateForm.resetFileds();
                        })
                    }
                })
            },
            reset_methods:function(e) {
                var telstr = sessionStorage.getItem('telephone');
                this.DateForm.tel=telstr;
                var emailstr = sessionStorage.getItem('email');
                if(emailstr != "null") {
                    this.DateForm.email=emailstr;
                }
                var genderstr = sessionStorage.getItem('gender')
                if(genderstr){
                    this.DateForm.sex = "男";
                }else {
                    this.DateForm.sex = "女";
                }
                var namestr = sessionStorage.getItem('username')
                this.DateForm.username=namestr;
            }
    	}
  	}
</script>