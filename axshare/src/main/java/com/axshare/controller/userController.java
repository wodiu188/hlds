package com.axshare.controller;


import com.axshare.entity.Student;
import com.axshare.entity.Subject;
import com.axshare.entity.User;
import com.axshare.mapper.StudentMapper;
import com.axshare.mapper.UserMapper;
import com.axshare.utils.R;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;


import java.util.Date;
import java.util.HashMap;
import java.util.List;

@Controller
@ResponseBody
@CrossOrigin("*")
@RequestMapping("/axshare/user")
public class userController {
    @Autowired
    StudentMapper studentMapper;

    @PostMapping("/addStudent")
    public R addStudent(@RequestBody Student student){
        student.setCreatetime(new Date());
        student.setModifytime(new Date());
        int insert = studentMapper.insert(student);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        map.put("key",1856);
        return R.ok(map);


    }
    @PostMapping("/updataStudent")
    public R updataStudent(@RequestBody Student student){
        student.setModifytime(new Date());
        studentMapper.updateById(student);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        return R.ok(map);
    }

    @PostMapping("/deleteStudent")
    public R deleteStudent(@RequestParam(value = "id") int id){

        studentMapper.deleteById(id);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        return R.ok(map);
    }

    @GetMapping("/selectAllStudent")
    public R allStudent(){
        QueryWrapper<Student> objectQueryWrapper = new QueryWrapper<>();
        List<Student> students = studentMapper.selectList(objectQueryWrapper);
        HashMap<String, Object> map = new HashMap<>();
        map.put("code",20000);
        map.put("data",students);
        System.out.println(students);
        return R.ok(map);
    }


    //        System.out.println(username);
//        System.out.println(password);
//        QueryWrapper<User> queryWrapper = new QueryWrapper<>();
//        queryWrapper.eq("username", username).and(i->i.eq("password",password));
//        User user = userMapper.selectOne(queryWrapper);
//        HashMap<String, Object> map = new HashMap<>();
//        HashMap<String, Object> map2 = new HashMap<>();
//
//
//        if(user!=null) {
//            map2.put("token","admin-token");
//            map2.put("data",user);
//            map.put("data", map2);
//            map.put("code",20000);
//            return R.ok(map);
//        }
//        else
//            return R.error();
}
