import { Component, Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { UsersService } from '../users.service';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.css']
})
export class PopupComponent {

  constructor(private router: Router,private userService: UsersService) {}

  onsave(){
    this.router.navigate(['/loginn']);

      }

  }




