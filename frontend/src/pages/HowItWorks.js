import React from 'react';
import './HowItWorks.css';

const HowItWorks = () => {
  return (
    <div className="how-it-works-page">
      <section className="hiw-hero">
        <h1>Simplify Your Workflow in 3 Easy Steps</h1>
        <p>Our AI-powered Todo App makes managing your tasks intuitive and efficient.</p>
      </section>

      <section className="steps-section">
        <div className="step-card">
          <div className="step-icon">1</div>
          <h2>Sign Up & Personalize</h2>
          <p>Create your free account in seconds. Customize your preferences, set up categories, and tell our AI about your goals for a tailored experience.</p>
          <img src="https://via.placeholder.com/300x200/39FF14/000000?text=Quick+Signup+%26+Setup" alt="Quick Signup & Setup" />
        </div>

        <div className="step-card">
          <div className="step-icon">2</div>
          <h2>Add Tasks & Let AI Assist</h2>
          <p>Easily input your tasks. Our intelligent system will provide smart suggestions for prioritization, deadlines, and related resources, helping you stay organized.</p>
          <img src="https://via.placeholder.com/300x200/39FF14/000000?text=AI-Powered+Task+Entry" alt="AI-Powered Task Entry" />
        </div>

        <div className="step-card">
          <div className="step-icon">3</div>
          <h2>Track Progress & Achieve Goals</h2>
          <p>Monitor your progress with insightful analytics. Mark tasks as complete, review your achievements, and watch your productivity soar as you conquer your to-do list.</p>
          <img src="https://via.placeholder.com/300x200/39FF14/000000?text=Goal+Tracking+%26+Analytics" alt="Goal Tracking & Analytics" />
        </div>
      </section>

      <section className="hiw-call-to-action">
        <h2>Ready to Supercharge Your Productivity?</h2>
        <p>Join thousands of happy users who are transforming their daily routines with our app.</p>
        <button className="button-primary">Get Started Now</button>
      </section>
    </div>
  );
};

export default HowItWorks;