using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Code4GoodRefugeeMentorMentee.Models;

namespace Code4GoodRefugeeMentorMentee.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }

        public IActionResult SignUp()
        {
            ViewData["Message"] = "Your application description page.";

            return View();
        }

        public IActionResult TeacherSignUp()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult StudentSignUp()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult Dashboard()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult SearchPage()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult SearchResults()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult ViewProfile()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }

        public IActionResult EditDashboard()
        {
            ViewData["Message"] = "Your contact page.";

            return View();
        }
    }
}