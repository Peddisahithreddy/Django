import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MyServiceService } from '../my-service.service';
import { UsersService } from '../users.service';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  logo="../assets/astreya-logo.jpeg"
  username : string = '';
  password : string = '';
  Data:any[] = [];
  constructor(private router: Router, private authService: MyServiceService,private userService: UsersService) {}
  ngOnInit(){

    this.userService.getUsers().subscribe((data)=>{
    this.Data= data;

  })
}
  onsave() {
    // Perform your authentication logic here.
    this.authService.login(this.username, this.password).subscribe((response) => {
      // Handle the response from the backend, e.g., set user authentication status, navigate to another page, etc.
      console.log(response);
      this.router.navigate(['/user']);
    });

    // For simplicity, let's assume validation always succeeds.
    // In a real application, you'd check user credentials against a backend service.

    // Redirect to the home page upon successful login.

  }
}



