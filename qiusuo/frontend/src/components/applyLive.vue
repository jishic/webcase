<template>
    <el-container>
        <el-aside>
            <el-row class="tac">
                <el-col :span="20">
                    <el-menu default-active="4" class="el-menu-vertical-demo">
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
                        <el-menu-item index="4" @click = "move4">
                            <i class="el-icon-bell"></i>
                            <span slot="title">申请直播间</span>
                        </el-menu-item>
                    </el-menu>
                </el-col>
            </el-row> 
        </el-aside>
        <el-main>
            <el-form ref="applyLiveForm" :model="applyLiveForm" label-width="110px" :rules="rules"> 
                <el-form-item label="上传直播间封面">
                    <el-input type="file" name="file" id="file_upload"></el-input>
                </el-form-item>
                <el-form-item label="房间名" prop="roomName">
                    <el-input v-model="applyLiveForm.roomName"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="apply_method">申请直播间</el-button>
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
            var validateRn = (rule, value, callback) => {    
                value=value.toLowerCase()
                if (value === '') {
                    callback(new Error('请输入房间名称'));
                }else {
                    callback();
                }
            };
            return {
                applyLiveForm: {
                    roomName: '',
                    whether:'No'
                },
                rules: {
                    roomName: [{
                        required: true,
                        validator: validateRn,
                        trigger: 'blur'
                    }],
                }
            };
        },
        created() {
            var istea = sessionStorage.getItem('isTea');
            if(istea != 'true') {
                this.$router.push({
                    name: 'lifestreem',
                    params: {
                    }
                })                
            }
        },
        methods: {
            move1:function(){
                this.$router.push({
                    name: 'PersonalDate',
                    params: {
                    }
                })
            },
            move2:function(){
                this.$router.push({
                    name: 'ChangePassword',
                    params: {
                    }
                })
            },
            move3:function(){
                const url = getUrl('backend/focuslist')//127.0.0.1
                //const url = '/backend/focuslist'//mock
                var params = new URLSearchParams()
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
                    }                    
                })
            },
            apply_method:function(){
                this.$refs.applyLiveForm.validate((valid) =>{
                    if(valid) {
                        const url = getUrl('backend/startstream') //后台的URL
                        var form_data = new FormData();
                        var file_info =$( '#file_upload')[0].files[0];
                        form_data.append('image',file_info);
                        var username = sessionStorage.getItem('username');
                        form_data.append('username', username);
                        form_data.append('roomName', this.applyLiveForm.roomName);
                       
                        if(this.applyLiveForm.whether === "Yes")
                        {
                            form_data.append('whether', true)
                        }
                        else {
                            form_data.append('whether', false)
                        }
                        this.$axios({
                            method: 'post',
                            url: url,
                            data: form_data
                        }).then((res) => {
                            if(res.data.success) {
                                sessionStorage.setItem('roomnum',res.data.roomnum);
                                sessionStorage.setItem('roomtitle',res.data.roomtitle);
                                var len = res.data.stuimgpath.length;
                                sessionStorage.setItem('stuimgpath',res.data.stuimgpath.substring(10,len));
                                this.$message.success('申请直播间成功,正在跳转至直播间');
                                this.$router.push({
                                    name: 'studio',
                                    params: { 
                                    }
                                })
                            }
                            else {
                                this.$message.error('申请直播间失败');
                            }
                            this.$refs.applyLiveForm.resetFileds();
                        })
                    }
                })  
            }
        }
    }
</script>