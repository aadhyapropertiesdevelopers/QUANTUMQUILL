from flask import Flask, render_template

app = Flask(__name__)


# Route for the Home page (you can customize this as well)
@app.route('/')
def home():
    return render_template('home.html')

# Route for the Products page
@app.route('/products')
def products():
    # Define product information
    product_list = [
        {
            'name': 'QuantumQuill ERP',
            'description': 'A comprehensive enterprise resource planning system designed to streamline operations.',
            'features': ['Automates business processes', 'Customizable to business needs', 'Real-time data analytics'],
            'image': 'erp.jpg'
        },
        {
            'name': 'QuantumQuill CRM',
            'description': 'A customer relationship management platform to boost your sales and marketing efforts.',
            'features': ['Track customer interactions', 'Manage sales pipelines', 'Automate marketing campaigns'],
            'image': 'crm.jpg'
        },
        {
            'name': 'QuantumCloud Storage',
            'description': 'Secure, scalable cloud storage solutions for businesses of all sizes.',
            'features': ['Access from anywhere', 'High-level encryption', 'Automatic backup'],
            'image': 'cloud_storage.jpg'
        },
        {
            'name': 'QuantumShield',
            'description': 'A cybersecurity suite designed to protect your network and data.',
            'features': ['Threat detection and prevention', 'Real-time monitoring', 'Automated security updates'],
            'image': 'shield.jpg'
        }
    ]
    
    return render_template('products.html', products=product_list)

# Route for the Services page
@app.route('/services')
def services():
    # Define services information
    service_list = [
        {
            'name': 'Consulting & IT Strategy',
            'description': 'Tailored IT strategies and digital transformation consulting to drive your business forward.',
            'details': ['IT Strategy Planning', 'Digital Transformation Consulting', 'Custom Solutions Design']
        },
        {
            'name': 'Custom Software Development',
            'description': 'Creating bespoke software solutions that meet your business needs.',
            'details': ['End-to-end development', 'Mobile & Web applications', 'Enterprise Solutions']
        },
        {
            'name': 'Cloud Services',
            'description': 'Migration, optimization, and management of your cloud infrastructure.',
            'details': ['Cloud Migration', 'Cloud Infrastructure Management', 'Cloud Security']
        },
        {
            'name': 'Cybersecurity Services',
            'description': 'Protecting your business from online threats with our comprehensive cybersecurity offerings.',
            'details': ['Threat Assessment & Penetration Testing', 'Incident Response', 'Security Audits & Compliance']
        }
    ]
    
    return render_template('services.html', services=service_list)

if __name__ == '__main__':

    app.run(debug=True)