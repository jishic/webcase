<template>
    <div class="conatiner">
        <el-col :span="18">
             <div class="grid-content">
                <board></board>
             </div>
        </el-col>
        <el-col :span="6">
            <div class="grid-content">
            </div>
        </el-col>
    </div>
</template>

    
<script>
import board from "./complexboard";
export default {
  name: "room",
  components: {
    board
  }
};
</script>
<style scoped></style>