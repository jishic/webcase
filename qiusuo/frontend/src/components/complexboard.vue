<template>
	<div class="container">
		<el-tabs type="border-card">
			<el-tab-pane label="Editor">
				<editor v-model="content" @init="editorInit" lang="html" theme="monokai" width="800" height="480"></editor>
			</el-tab-pane>
			<el-tab-pane label="PPT">
				<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQmL7yggtf0jUPQAJsAcsK2UsNvPv49DhnMKbU-gqdjOnDySr3qRFRAuOsdHkl_I8-EDA1PDSLWd-0R/embed?start=false&loop=false&delayms=10000&slide=id.gd251bb473_0_600" frameborder="0" width="800" height="480" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
			</el-tab-pane>
		</el-tabs>
	</div>
</template>

<script>
export default{
	components: {
		editor: require('vue2-ace-editor')
	},
	data() {
		return {
			content:""
		}
	},
	methods: {
		editorInit: function () {
            require('../../node_modules/brace/mode/html')
            require('../../node_modules/brace/mode/javascript')
            require('../../node_modules/brace/mode/less')
            require('../../node_modules/brace/theme/monokai')
        }
    }
}
</script>

<style scoped>
.container{
	width: 818px;
	height: 500px;
}
</style>


</style>