import { Component, Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { UsersService } from '../users.service';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-popup',
  templateUrl: './popup.component.html',
  styleUrls: ['./popup.component.css']
})
export class PopupComponent {
  users: any[] = [];

  constructor(private router: Router,private userService: UsersService) {}

  onsave(){

      this.router.navigate(['/loginn']);

      }

  }




