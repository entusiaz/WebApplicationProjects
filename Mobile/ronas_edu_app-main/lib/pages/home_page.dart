// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:ronas_edu_app/utils/my_card.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[300],
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: EdgeInsets.symmetric(horizontal: 25.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Profile image
                  Container(
                    child: Center(
                      child: CircleAvatar(
                        radius: 27,
                        backgroundColor: Colors.black,
                        child: CircleAvatar(
                          backgroundImage: AssetImage('lib/images/gift-cr.jpg'),
                          radius: 25,
                        ),
                      ),
                    ),
                  ),

                  // Connect button
                  Container(
                    height: 50,
                    width: 200,
                    decoration: BoxDecoration(
                      color: Colors.black,
                      borderRadius: BorderRadius.circular(50),
                    ),
                    child: Center(
                      child: Padding(
                        padding: EdgeInsets.fromLTRB(20, 5, 20, 5),
                        child: Text(
                          'Connect to class',
                          style: TextStyle(
                              fontFamily: 'Helvetica',
                              fontSize: 16.0,
                              fontWeight: FontWeight.w600,
                              color: Colors.white),
                        ),
                      ),
                    ),
                    // padding: EdgeInsets.all(10),
                  ),
                  // ignore: avoid_unnecessary_containers
                ],
              ),
            ),

            SizedBox(
              height: 25,
            ),

            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 25.0),
              child: Container(
                child: Row(
                  children: [
                    Text(
                      'Nice streak, Andrew',
                      style: TextStyle(
                        color: Colors.black,
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            ),

            SizedBox(
              height: 25,
            ),

            Container(
              height: 200,
              child: Row(
                children: [
                  MyCard(
                    title: 'Days in trainning',
                    number: '255',
                    count: '24 days in a row',
                    color: Colors.greenAccent,
                  ),
                  MyCard(
                    title: 'Completed Courses',
                    number: '12',
                    count: '2 in this month',
                    color: Colors.amberAccent,
                  ),
                ],
              ),
            )
            // welcome text

            // summary boxes

            // List Todays classes

            // Class box: Title, Status, Teacher, Icon

            // Class box
          ],
        ),
      ),
    );
  }
}
