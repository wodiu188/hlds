package com.axshare;

import com.axshare.entity.User;
import com.axshare.mapper.UserMapper;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class AxshareApplicationTests {

    @Autowired
    UserMapper userMapper;

    @Test
    void contextLoads() {
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("username","111").and(i->i.eq("password","222"));
         System.out.println(userMapper.selectOne(queryWrapper));
    }

}
