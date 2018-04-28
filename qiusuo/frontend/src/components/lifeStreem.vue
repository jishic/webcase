<template>
		<div class="all">
				<!-- 轮播 + 中栏 + 视频显示  -->
				<carousel></carousel>
				<div class="choose">
						<el-row>
								<el-button round size="mini" class="hotbtn" @click="usehotSort">按热度排行</el-button>
								<el-button round size="mini" class="timebtn" @click="usetimeSort">按时间排行</el-button>
								<div class="titlefont">精选视频</div>
						</el-row>
				</div>
				<div class="container">
						<div class="single" v-for="item in sorteditems" :key='item.title'>
								<a href="#" clss="link">
										<div class="innerimg">
												<td><img :src="item.stuimgpath" class="img" width="300" height="200" /></td>
										</div>
										<div class="course-body">
												<div class="singlecontent">
														{{item.roomtitle}}
												</div>

												<div class="singlefooter">
														<i class="el-icon-view footerchar">&nbsp;{{item.teachername}}</i>
														<span class="course-money">free</span>
												</div>
										</div>
								</a>  
						</div> 
				</div>
				<!-- 分页 -->
				<div class="pageblock">
						<el-pagination background="#409eff" layout="prev, pager, next" :total="90"></el-pagination>
				</div>
		</div>
</template>

<script >
import carousel from "./carousel";
import getUrl from '../api/getPath'
export default {
	name: "lifeStreem",
	components: {
		carousel
	},
	data() {
		return {
			hotflag: true,
			items: []
		};
	},
	created(){
			this.itemsList();
	},
	methods: {
		usehotSort: function(self) {
			this.hotflag = true;
		},
		usetimeSort: function(self) {
			this.hotflag = false;
		},
		itemsList:function(){
				const url = getUrl('backend/liveroomlistis')
				alert()
						var params = new URLSearchParams()
						this.$axios({
										method: 'post',
										url: url,
										data: params  //get params     post data
										}).then((res) => {
										if(res.data.success){
												this.items=res.data.information
										}
										})
		}
	},
	computed: {
		sorteditems: function() {
			if (this.hotflag === true) {
				function compareHot(a, b) {
					if (a.hot < b.hot) return 1;
					if (a.hot > b.hot) return -1;
					return 0;
				}
				return this.items.sort(compareHot);
			} else {
				function compareTime(a, b) {
					if (a.time < b.time) return 1;
					if (a.time > b.time) return -1;
					return 0;
				}
				return this.items.sort(compareTime);
			}
		}
	}
};
</script>


<style scoped>
/* 直播item */

.all {
	background-color: #f7f7f7;
	height: 1400px;
}
.choose {
	width: all;
	height: 100px;
	background: #f7f7f7;
}

.titlefont {
	margin-top: 2.4%;
	margin-right: 36%;
	display: inline;
	font-size: 33px;
	float: right;
	font-family: Hiragino Sans GB;
	color: #565656;
}
.timebtn {
	margin-top: 3%;
	float: right;
	margin-right: 0.5%;
}

.hotbtn {
	margin-top: 3%;
	float: right;
	margin-right: 23%;
}
.container {
	width: 70%;
	margin-top: 2%;
	padding-left: 23%;
	padding-right: 20%;
	background-color: #f7f7f7;
}
.single {
	display: inline-block;
	margin-right: 5%;
	margin-bottom: 3%;
	padding-left: 5px;
	padding-right: 5px;

	transition: all 0.2s;
}

.single:hover {
	box-shadow: 5px 5px 5px 3px #e5e5e5;
	transform: scale(1.05);
}

.link {
	text-decoration: none;
}

.singlecontent {
	text-align: center;
	font-family: Hiragino Sans GB;
	color: #565656;
	text-decoration: none;
}

.singlefooter {
	font-family: Hiragino Sans GB;
	color: #565656;
	padding-bottom: 10px;
}

.footerchar {
	padding-top: 2%;
}

.course-money {
	padding: 3px 10px;
	color: #fff;
	border-radius: 100px;
	background-color: #59cf4a;
	float: right;
}

/*分页效果*/
.pageblock {
	margin-left: 40%;
}
</style>