<template>
    <el-container>
        <el-aside>
     	    <el-row class="tac">
                <el-col :span="20">
            		<el-menu default-active="3" class="el-menu-vertical-demo">
                		<el-menu-item index="1" @click = "move1">
                    		<i class="el-icon-edit"></i>
                    		<span slot="title" >个人资料</span>
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
            <div class="single" v-for="item in items">
                <a href="#" clss="link">
                    <div class="innerimg">
                        <td><img :src="item.imgpath" class="img" width="300" height="250" /></td>
                    </div>
                    <div class="course-body">
                        <div class="singlecontent">
                            {{item.name}}
                        </div>
                        <div class="singlefooter">
                            <i class="el-icon-view footerchar">&nbsp;300</i>
                            <el-button type="warning" class="cancel-focus" plain @click="cancel_method(item.name)">取消关注</el-button>
                        </div>
                    </div>
                </a>  
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
    margin-top: 50px;
}
.el-input {
  	width: 300px;
}
.container{
    width: 70%;
    margin-top: 2%;
    padding-left: 23%;
    padding-right: 20%;
    background-color: #f7f7f7;
}
.single{
    display: inline-block;
    margin-right: 1%;
    margin-bottom: 3%;
    padding-left: 5px;
    padding-right: 5px;  
    transition: all 0.2s; 
}
.single:hover{
    box-shadow: 5px 5px 5px 3px #e5e5e5;
    transform: scale(1.05)
}
.link{
    text-decoration: none;
}

.singlecontent{
    text-align: center;
    font-family: Hiragino Sans GB;
    color: #565656;
    text-decoration: none;
}
.singlefooter{
    font-family: Hiragino Sans GB;
    color: #565656;
    padding-bottom: 10px;
}
.cancel-focus{
    float: right;
}
</style>

<script>
    import 'element-ui/lib/theme-chalk/index.css';
    import 'vue/dist/vue.js'
    import axios from '../api/axios'
    import getUrl from '../api/getPath'
  	export default {
  	    data() {
      		return {
                istea:'',
                items:[],
      		};
    	},
        created() {
            this.items = JSON.parse(sessionStorage.getItem('focuslist'));
            var istea = sessionStorage.getItem('isTea');
            if(istea === "false") {
                this.istea = false;
            }else {
                this.istea = true;
            }
        },
  	    methods: {
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
            cancel_method:function(name) {
                        const url = getUrl('backend/acattentionrl')
                        var params = new URLSearchParams()
                        var username = sessionStorage.getItem('username')
                        params.append('username',username);
                        params.append('teachername', name)
                        this.$axios({
                            method: 'post',
                            url: url,
                            data: params
                        }).then((res) => {
                            if(res.data.success) {
                                this.$message.success('取消关注成功');
                                this.items = res.data.attentionList;
                            }
                            else {
                                this.$message.error('取消关注失败');
                            }
                            this.$refs.DateForm.resetFileds();
                        })
            }
    	}
  	}
</script>