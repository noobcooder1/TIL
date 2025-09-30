import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(

        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        backgroundColor: Theme.of(context).colorScheme.inversePrimary,

        title: Text(widget.title),
      ),

body: Column(

  mainAxisAlignment: MainAxisAlignment.center,
  children: [
    createBody1(),
    SizedBox(height: 20),
    createBody2(),
    SizedBox(height: 20),
    createBody3(),
    SizedBox(height: 30),
    craateBody5(),
  ],
),
      
    );
  }

  Widget createBody1() {
    return Container(
      width: 200,
      height: 100,
      color: Colors.red,
      alignment: Alignment.center,
      child: Text('Container'),
    );
  }

Widget createBody2() {
  return Container(
    padding: const EdgeInsets.only(
      left: 20,
      right: 20,
    ),
    decoration: BoxDecoration(
      gradient: LinearGradient(
        colors: [
          Color.fromARGB(255, 100, 200, 200),
          Color.fromARGB(255, 50, 100, 150),
        ],
      ),
      boxShadow: [
        BoxShadow(
          color: Colors.blue.withOpacity(0.2),
          spreadRadius: 10,
          blurRadius: 6,
          offset: Offset(0, 3),
        ),
      ],
    ),
    width: 200,
    height: 150,
    child: Center(
      child: Text(
        'Container',
        style: TextStyle(color: Colors.white),
      ),
    ),
  );  
}

Widget createBody3() {
  return Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
      Expanded(
        child: Container(
          height: 50,
          color: Colors.purple,
          margin: const EdgeInsets.all(6),
          ),
        ),
      ],
    );
}

Widget craateBody5()
{
  return Row(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
    children: [
      Expanded(
        flex: 3,
        child: Container(
         height: 50,
         color: Colors.green,
         margin: const EdgeInsets.all(8)
         ),
        ),
        Expanded(
        flex: 3,
        child: Container(
         height: 50,
         color: Colors.orange,
         margin: const EdgeInsets.all(8)
          ),
         ),
         ]
  );
  }
}