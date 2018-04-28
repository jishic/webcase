<template>
	<div class="block">
		<el-carousel height="520px">
			<el-carousel-item v-for="item in imgs" :key="item">
				<div class="imgcap">
					<img :src="item.url">
				</div>
			</el-carousel-item>
		</el-carousel>
	</div>
	

</template>

<script>
export default{
	name: 'carousel',
	data(){
		return {
			imgs:[
			{
				url: require('../assets/car1.png')
			},
			{
				url: require('../assets/car2.png')
			}
			]
		}
	}
}
</script>

<style>
.el-carousel__item h3 {
	color: #475669;
	font-size: 14px;
	opacity: 0.75;
	line-height: 150px;
	margin: 0;
}

.el-carousel__item:nth-child(2n) {
	background-color: #2c3335;
}

.el-carousel__item:nth-child(2n+1) {
	background-color: #665bbb;
}
.imgcap{
	text-align: center;
}
</style>