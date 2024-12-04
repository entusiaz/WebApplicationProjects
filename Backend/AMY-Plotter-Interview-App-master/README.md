![](company-logo.jpg)

# AMY Plotter Interview App

> ### A Django REST framework project that takes geometric coordinates with POST method to the plot figures in XML/SVG format.

This repo is an interview test project — corrections, observations, PR's and issues are gladly welcome!

## How it Works

​The client makes a JSON POST request to the API. The JSON object will contain `geometry` and `plane` attributes.

- `geometry` describes the coordinates of the figure to be plotted

- `plane` describes the plane of the figure

### Sample input:

```json
{
  "geometry": [
    { "x1": -207, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 18 },
    { "x1": -207, "x2": -332, "y1": 209, "y2": 391, "z1": 0, "z2": 18 },
    { "x1": 207, "x2": 332, "y1": 9, "y2": 191, "z1": 0, "z2": 18 },
    { "x1": 207, "x2": 332, "y1": 209, "y2": 391, "z1": 0, "z2": 18 },
    { "x1": -8, "x2": 10, "y1": 9, "y2": 191, "z1": 0, "z2": 320 },
    { "x1": -8, "x2": 10, "y1": 209, "y2": 391, "z1": 0, "z2": 320 },
    { "x1": -350, "x2": -332, "y1": 9, "y2": 191, "z1": 0, "z2": 320 },
    { "x1": -350, "x2": -332, "y1": 209, "y2": 391, "z1": 0, "z2": 320 },
    { "x1": 332, "x2": 350, "y1": 9, "y2": 191, "z1": 0, "z2": 320 },
    { "x1": 332, "x2": 350, "y1": 209, "y2": 391, "z1": 0, "z2": 320 },
    { "x1": -350, "x2": 350, "y1": 391, "y2": 409, "z1": 0, "z2": 320 },
    { "x1": -350, "x2": 350, "y1": 191, "y2": 209, "z1": 0, "z2": 320 },
    { "x1": -350, "x2": 350, "y1": -9, "y2": 9, "z1": 0, "z2": 320 }
  ],
  "plane": "XY"
}
```

​

The API gives an output containing the figure in SVG-format.

### Sample output:

```xml
<svg baseProfile="full" height="100%" version="1.1" viewBox="-450,-109,900,618" width="100%" xmlns="http://www.w3.org/2000/svg">
    <defs/>
    <rect fill="gray" height="182" stroke="black" width="-125" x="-207" y="9"/>
    <rect fill="gray" height="182" stroke="black" width="-125" x="-207" y="209"/>
    <rect fill="gray" height="182" stroke="black" width="125" x="207" y="9"/>
    <rect fill="gray" height="182" stroke="black" width="125" x="207" y="209"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="-8" y="9"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="-8" y="209"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="-350" y="9"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="-350" y="209"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="332" y="9"/>
    <rect fill="gray" height="182" stroke="black" width="18" x="332" y="209"/>
    <rect fill="gray" height="18" stroke="black" width="700" x="-350" y="391"/>
    <rect fill="gray" height="18" stroke="black" width="700" x="-350" y="191"/>
    <rect fill="gray" height="18" stroke="black" width="700" x="-350" y="-9"/>
</svg>
```

## Installation

1. Create a new directory and install [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
2. Activate the virtualenv: `source venv/bin/activate`
3. Clone this repository: `git clone git@github.com:J-rayX/amy_plotter.git`.

4. `cd` into `amy_plotter`: `cd amy_plotter`.

5. Install required packages: `pip install -r requirements.txt`.

6. Run the internal Django server: `python manage.py runserver`.

If all went well then your command line prompt should now end with

```
Django version 3.1.4, using settings 'amy_plotter.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

- You may use [Postman](https://www.postman.com/product/api-client/) for testing endpoints

You may reach out to me for further inquiry and discussion via jkaylight@gmail.com
