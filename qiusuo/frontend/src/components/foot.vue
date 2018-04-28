<template>
<div class="foot">
    <div class="foot_first">
    <el-row class="el_sty">
    <el-col :span="5" class="div_mar"><div class="grid-content bg-purple-light">
        <div class="icon">
        <img id ="img" src="../assets/logo.png" class="img_icon">
        <span class="first_span">双子楼<p class="english">shuangzilou.com</p></span>
        </div>
        <p class="first_p">学技术，来合工大</p>
        </div></el-col>
    <el-col :span="3" class="div_mar"><div class="grid-content bg-purple">
        <div class="col-title">公司</div>
        <a href="">关于我们</a><br>
        <a href="">联系我们</a><br>
        <a href="">加入我们</a><br>
        </div></el-col>
    <el-col :span="3" class="div_mar"><div class="grid-content bg-purple-light">
        <div class="col-title">合作</div>
        <a href="">我要投稿</a><br>
        <a href="">教师合作</a><br>
        <a href="">高校合作</a><br>
        <a href="">友情链接</a><br>
        <a href="">开发者</a><br>
        </div></el-col>
    <el-col :span="3" class="div_mar"><div class="grid-content bg-purple">
        <div class="col-title">服务</div>
        <a href="">企业版</a><br>
        <a href="">实战训练营</a><br>
        <a href="">会员服务</a><br>
        <a href="">实验报告</a><br>
        <a href="">常见问题</a><br>
        <a href="">隐私条款</a>
        </div></el-col>
    <el-col :span="3" class="div_mar"><div class="grid-content bg-purple-light">
        <div class="col-title">学习路径</div>
        <a href="">Python学习路径</a><br>
        <a href="">Linux学习路径</a><br>
        <a href="">大数据学习路径</a><br>
        <a href="">Java学习路径</a><br>
        <a href="">PHP学习路径</a><br>
        <a href="">全部</a>
        </div></el-col>
    </el-row>
    </div>
    <div class="copyright">Copyright @2018 双子楼在线直播教育 | 合工大翡翠湖校区</div>
</div>
</template>

<script>
export default{
	data(){
   		return {
			
		}
	}
}
</script>

<style scoped>
.foot{
    height: 264px;
    background: rgb(23,25,25);
    font-family: "Microsoft Yahei","Helvetica Neue",Helvetica,Arial,sans-serif;
    
}
 .foot_first{
    height: 214px;
    width: 100%;
    background: rgb(51,51,51);
}
.el_sty{
    margin-left: 400px;
}
.div_mar{
    margin-top: 20px;
    
}
.img_icon{
    height: 50px;
    width: 40px;
    float: left;
}
.first_span{
    margin-top: 3px;
    margin-left: 5px;
    color: white;
    font-size: 25px;
    float: left;    
}
.first_p{
    margin-top: 4px;
    color: rgb(8,191,145);
    font-size: 27px;
}
.col-title{
    color:#8c9999;
    margin-bottom: 10px;
    font-size: 20px;
}

.el-col a{
    color: #8c9999;
    text-decoration: none;
    font-size: 13px;
}
.english{
    font-size: 5px;
    margin-top: -2px;
}
.icon{
    height: 60px;
}

a:hover{
    color: white;
}
.copyright{
    text-align: center;
    margin-top: 10px;
    color: #8c9999;
} 
</style>