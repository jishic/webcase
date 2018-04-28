<template>
<div>
        <input type="file" name="file" id="file_upload">
        <input type="button" value="上传" @click="FileUpload">
        <img src="../../../backend/image/9708lamu.jpg">
</div>
</template>
<script>
import getUrl from '../api/getPath'
export default {
    methods: {
    FileUpload:function() {
            
            var form_data = new FormData();
            var file_info =$( '#file_upload')[0].files[0];
            alert(file_info.name)
            form_data.append('image',file_info);
            form_data.append('username',"wwk")
            var url=getUrl('backend/fileupload');
            this.$axios({
                method: 'post',
                url: url,
                data: form_data  //get params     post data
                }).then((res) => {
                })
    }
    }
}
</script>
<style>

</style>
