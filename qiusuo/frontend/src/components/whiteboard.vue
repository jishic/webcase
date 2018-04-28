<template>
	<div>
		<div id="tool" >
			<ul>
				<li @click = "qianbi" ref="qianbi" class="choice"><img src="../assets/qianbi.png"/></li>
				<li @click="yuan" ref="yuan"><img src="../assets/yuanxing.png"/></li>
				<li @click="juxing" ref="juxing" ><img src="../assets/juxing.png"/></li>
				<li @click="xiangpi" ref="xiangpi"><img src="../assets/xiangpi.png"/></li>
				<li @click="black" ref = "black" class="black choice"></li>
				<li @click="red" ref = "red" class="red"></li>
				<li @click="yellow" ref ="yellow" class="yellow"></li>
				<li @click="xi" ref="xi" class="zi choice">细</li>
				<li @click="cu" ref="cu" class="zi">粗</li>
				<el-tag type="warning" @click.native="clear">清空</el-tag>
			</ul>
		</div>
		<div id = "wb">
			<canvas ref="canvas"  width = "700px" height = "600px" style @mousedown = "draw($event)"></canvas>
			<canvas ref="canvas2"  width = "700px" height = "600px"  @mousedown = "draw($event)"></canvas>
		</div>
	</div>
</template>

<style scoped>
	canvas
	{
		position: absolute;
		left: 0px;
		right: 0px;
	}
	#tool
	{
		width: 90px;
		height: 601px;
		border-top: 1px solid black;
		border-right: 1px solid black;
		border-bottom: 1px solid black;
		float:left;
		background-color:rgb(220,230,244) ;
	}
	#wb
	{
		width: 701px;
		height: 601px;
		position: relative;
		float:left;
		border: 1px solid black;
	}
	ul
	{
		background-color: rgb(220,230,244);
		text-align: center;
		margin: 0;
		padding: 0;
		height: 50px;
		float: left;
		margin-left: 10px;
	}
	img {
		width: 50px;
		height: 50px;
	}
	ul>li
	{
		width: 50px;		
		height: inherit;
		margin-top: 5px;
		display: inline-block;
		text-align:center;
	}
	.choice
	{
		border: 3px solid gold;
	}
	.red
	{
		background-color: red;
	}
	.black
	{
		background-color: black;
	}
	.yellow
	{
	background-color: yellow;
	}
	.zi
	{
		font-size: 20px;
	}
</style>

<script>
    import 'element-ui/lib/theme-chalk/index.css';
    import 'vue/dist/vue.js'
	let style = 0;
	let mycolor = "black";
	let mywidth = 2.5;
	export default {
		data() {
		},
		mounted() {
		},
		methods: {
			draw(e) {
				var canvas=this.$refs.canvas;
				var context=canvas.getContext("2d");
				var canvas2=this.$refs.canvas2;
				var context2=canvas2.getContext("2d");
				//e=e||window.event;
				e=this.touch ? e.touches[0] : e;
				var beginx =e.offsetX;
				var beginy =e.offsetY;
				switch(style)
				{
					//铅笔状态
					case 0:
						document.onmousemove=function(e){		
							context.beginPath();
							context.moveTo(beginx,beginy);
							context.lineTo(e.offsetX,e.offsetY);		
							context.strokeStyle = mycolor;
							context.lineWidth = mywidth;
							context.stroke();
							beginx =e.offsetX;
							beginy =e.offsetY;
						}
						break;
					//矩形状态
					case 1:
						document.onmousemove=function(e){		
							context2.clearRect(0,0,700,600); 
							var xx=e.offsetX-beginx;
							var yy=e.offsetY-beginy;
							context2.beginPath();
							context2.rect(beginx,beginy,xx,yy);
							context2.strokeStyle = mycolor;
							context2.lineWidth = mywidth;
							context2.stroke();
						}
						break;
					//圆形状态
					case 2:
						document.onmousemove=function(e){		
							context2.clearRect(0,0,700,600); 					
							var xx=e.offsetX-beginx;
							var yy=e.offsetY-beginy;
							var r = Math.sqrt(xx*xx+yy*yy)/2;
							var centerx = (e.offsetX+beginx)/2;
							var centery = (e.offsetY+beginy)/2;
							context2.beginPath();
							context2.arc(centerx,centery,r,0,2*Math.PI,true);
							context2.strokeStyle = mycolor;
							context2.lineWidth = mywidth;
							context2.stroke();
						}
						break;
					//橡皮状态
					case 3:
						document.onmousemove=function(e){
							context.beginPath();
							context.moveTo(beginx,beginy);
							context.lineTo(e.offsetX,e.offsetY);
							context.strokeStyle = "white";
							context.lineWidth = mywidth*10;
							context.stroke();
							beginx =e.offsetX;
							beginy =e.offsetY;
						}
						break;
				}
				
				document.onmouseup=function(e){
					switch(style)
					{
						//铅笔
						case 0:
							document.onmousemove=document.onmouseup=null;
							break;
						//矩形
						case 1:
							context2.clearRect(0,0,700,600); 
							var xx=e.offsetX-beginx;
							var yy=e.offsetY-beginy;
							context.beginPath();
							context.rect(beginx,beginy,xx,yy);
							context.strokeStyle = mycolor;
							context.lineWidth = mywidth;
							context.stroke();
							document.onmousemove=document.onmouseup=null;
							break;
						//画圆
						case 2:
							context2.clearRect(0,0,700,600); 
							var xx=e.offsetX-beginx;
							var yy=e.offsetY-beginy;
							var r = Math.sqrt(xx*xx+yy*yy)/2;
							var centerx = (e.offsetX+beginx)/2;
							var centery = (e.offsetY+beginy)/2;
							context.beginPath();
							context.arc(centerx,centery,r,0,2*Math.PI,true);
							context.strokeStyle = mycolor;
							context.lineWidth = mywidth;
							context.stroke();
							document.onmousemove=document.onmouseup=null;
							break;
						//橡皮
						case 3:
							document.onmousemove=document.onmouseup=null;
							break;
					}		
				}	
			},
			qianbi() {
				style = 0;
				this.$refs.yuan.classList.remove('choice');
				this.$refs.qianbi.classList.add('choice');
				this.$refs.juxing.classList.remove('choice');
				this.$refs.xiangpi.classList.remove('choice');
			},
			juxing:function() {
				style = 1;
				this.$refs.yuan.classList.remove('choice');
				this.$refs.qianbi.classList.remove('choice');
				this.$refs.juxing.classList.add('choice');
				this.$refs.xiangpi.classList.remove('choice');
			},
			yuan() {
				style = 2;
				this.$refs.yuan.classList.add('choice');
				this.$refs.qianbi.classList.remove('choice');
				this.$refs.juxing.classList.remove('choice');
				this.$refs.xiangpi.classList.remove('choice');
			},
			xiangpi() {
				style = 3;
				this.$refs.yuan.classList.remove('choice');
				this.$refs.qianbi.classList.remove('choice');
				this.$refs.juxing.classList.remove('choice');
				this.$refs.xiangpi.classList.add('choice');
			},
			red(){
				mycolor = "red";
				this.$refs.red.classList.add('choice');
				this.$refs.black.classList.remove('choice');
				this.$refs.yellow.classList.remove('choice');
			},
			black(){
				mycolor = "black";
				this.$refs.red.classList.remove('choice');
				this.$refs.black.classList.add('choice');
				this.$refs.yellow.classList.remove('choice');
			},
			yellow(){
				mycolor = "yellow";
				this.$refs.red.classList.remove('choice');
				this.$refs.black.classList.remove('choice');
				this.$refs.yellow.classList.add('choice');
			},
			xi() {
				mywidth = 2.5;
				this.$refs.xi.classList.add('choice');
				this.$refs.cu.classList.remove('choice');
			},
			cu() {
				mywidth = 5;
				this.$refs.xi.classList.remove('choice');
				this.$refs.cu.classList.add('choice');
			},
			clear(){
				var canvas=this.$refs.canvas;
				var context=canvas.getContext("2d");
				context.clearRect(0,0,700,600);
			},
		}
	}
</script>