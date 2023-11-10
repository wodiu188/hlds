package com.axshare.controller;

import com.axshare.entity.User;
import com.axshare.mapper.UserMapper;
import com.axshare.utils.R;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@Controller
@ResponseBody
@CrossOrigin("*")
public class loginController {

    @Autowired
    UserMapper userMapper;

    @GetMapping("/Certification")
    public R userLogin(@RequestParam("username") String username,@RequestParam("password") String password){
        System.out.println(username);
        System.out.println(password);
        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("username", username).and(i->i.eq("password",password));
        User user = userMapper.selectOne(queryWrapper);
        HashMap<String, Object> map = new HashMap<>();
        HashMap<String, Object> map2 = new HashMap<>();


        if(user!=null) {
            map2.put("token","admin-token");
            map2.put("data",user);
            map.put("data", map2);
            map.put("code",20000);
            return R.ok(map);
        }
        else
            return R.error();
    }

}
