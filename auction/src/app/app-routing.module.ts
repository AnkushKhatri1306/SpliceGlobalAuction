import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AuthenticationComponent } from "./authentication/authentication.component";
import { HomeComponent } from "./home/home.component";

const routes: Routes = [
  {path: "login", component: AuthenticationComponent},
  {path: "home", component: HomeComponent},
  {path: "", redirectTo: "login", pathMatch: "full"}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
