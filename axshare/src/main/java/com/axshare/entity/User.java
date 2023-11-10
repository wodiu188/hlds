package com.axshare.entity;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@TableName
@Data
public class User {
    @TableField
    private String username;
    @TableField
    private String password;

}
