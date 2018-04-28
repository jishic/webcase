<template>
	<div>
		<div id="tool" >
			<ul>

			</ul>
		</div>
		<div id = "wb">
			<canvas ref="canvas"  width = "700px" height = "600px" style @mousedown = "draw($event)"></canvas>
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
			this.collert();
		},
		methods: {
			collert(){
	            var vm = this;
	            var signal = Signal("44bd67ed31d5485fb05bb2bc748dcaa7");
	            var session = signal.login("wwk4", "_no_need_token");
	            session.onLoginSuccess = function(uid){

	                var channel = session.channelJoin("123");
	                channel.onChannelJoined = function(){
	                    channel.onMessageChannelReceive = function(account, uid, msg){
							var myArray=new Array(7);
							myArray = msg;
	                        var beginx = myArray[0] ;
							var beginy = myArray[1];
							var offsetX = myArray[2];
							var offsetY = myArray[3];
							var style = myArray[4];
							var mycolor = myArray[5];
							var mywidth = myArray[6];
							var canvas=vm.$refs.canvas;
							var context=canvas.getContext("2d");
							switch(style)
							{
								//铅笔状态
								case 0:	
									context.beginPath();
									context.moveTo(beginx,beginy);
									context.lineTo(offsetX,offsetY);		
									context.strokeStyle = mycolor;
									context.lineWidth = mywidth;
									context.stroke();
									break;
								//矩形状态
								case 1:	
									var xx=offsetX-beginx;
									var yy=offsetY-beginy;
									context.beginPath();
									context.rect(beginx,beginy,xx,yy);
									context.strokeStyle = mycolor;
									context.lineWidth = mywidth;
									context.stroke();
									break;
								//圆形状态
								case 2:						
									var xx=offsetX-beginx;
									var yy=offsetY-beginy;
									var r = Math.sqrt(xx*xx+yy*yy)/2;
									var centerx = (offsetX+beginx)/2;
									var centery = (offsetY+beginy)/2;
									context.beginPath();
									context.arc(centerx,centery,r,0,2*Math.PI,true);
									context.strokeStyle = mycolor;
									context.lineWidth = mywidth;
									context.stroke();									
									break;
								//橡皮状态
								case 3:
									context.beginPath();
									context.moveTo(beginx,beginy);
									context.lineTo(offsetX,offsetY);
									context.strokeStyle = "white";
									context.lineWidth = mywidth*10;
									context.stroke();
									break;
								//清空
								case 4:
									context.clearRect(0,0,700,600);
									break;
							}
	                    }

	                };
	            };
	        },
		}
	}
</script>