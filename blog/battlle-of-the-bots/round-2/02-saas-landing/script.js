        console.log("Thou art a boil, a plague sore, an embossed carbuncle in my corrupted blood.");
        // GSAP Animations
        gsap.registerPlugin(ScrollTrigger, TextPlugin);
        
        // Navbar scroll effect
        gsap.to('.navbar-custom', {
            scrollTrigger: {
                trigger: 'body',
                start: 'top top',
                end: '100px top',
                scrub: true
            },
            background: 'rgba(15, 23, 42, 0.95)',
            backdropFilter: 'blur(25px)'
        });
        
        // Hero animations
        const tl = gsap.timeline();
        tl.from('.hero-badge', { duration: 0.8, y: 30, opacity: 0, ease: 'power2.out' })
          .from('.hero-title', { duration: 1, y: 50, opacity: 0, ease: 'power3.out' }, '-=0.3')
          .from('.hero-subtitle', { duration: 0.8, y: 30, opacity: 0, ease: 'power2.out' }, '-=0.5')
          .from('.btn-primary-gradient, .btn-outline-custom', { 
              duration: 0.8, 
              y: 20, 
              opacity: 0, 
              stagger: 0.2, 
              ease: 'back.out(1.7)' 
          }, '-=0.3');
        
        // Stats counter animation
        function animateCounter(element) {
            const target = parseInt(element.dataset.count);
            const duration = 2;
            const increment = target / (duration * 60); // 60 fps
            let current = 0;
            
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                element.textContent = Math.floor(current);
                if (target === 99.9) {
                    element.textContent = current.toFixed(1);
                }
            }, 1000 / 60);
        }
        
        // Trigger counter animation on scroll
        gsap.from('.stats-number', {
            scrollTrigger: {
                trigger: '.stats-card',
                start: 'top 80%',
                onEnter: () => {
                    document.querySelectorAll('.stats-number').forEach(animateCounter);
                }
            },
            duration: 0.8,
            y: 20,
            opacity: 0,
            stagger: 0.1
        });
        
        // Feature cards animation
        gsap.from('.feature-card', {
            scrollTrigger: {
                trigger: '#features',
                start: 'top 70%',
                stagger: 0.2
            },
            duration: 0.8,
            y: 50,
            opacity: 0,
            ease: 'power2.out'
        });
        
        // Pricing cards animation
        gsap.from('.pricing-card', {
            scrollTrigger: {
                trigger: '#pricing',
                start: 'top 70%',
                stagger: 0.2
            },
            duration: 0.8,
            y: 40,
            opacity: 0,
            ease: 'back.out(1.7)'
        });
        
        // Testimonial cards animation
        gsap.from('.testimonial-card', {
            scrollTrigger: {
                trigger: '#testimonials',
                start: 'top 70%',
                stagger: 0.1
            },
            duration: 0.6,
            scale: 0.9,
            opacity: 0,
            ease: 'back.out(1.7)'
        });
        
        // Demo functionality
        function runDemo() {
            const output = document.getElementById('demoOutput');
            const steps = [
                { icon: 'fas fa-user-plus', text: 'New customer "John Doe" registered', color: 'success', delay: 0 },
                { icon: 'fas fa-envelope', text: 'Welcome email sent successfully', color: 'info', delay: 1000 },
                { icon: 'fas fa-database', text: 'Customer data added to CRM', color: 'warning', delay: 2000 },
                { icon: 'fas fa-calendar', text: 'Follow-up call scheduled for Friday', color: 'primary', delay: 3000 },
                { icon: 'fas fa-check-circle', text: 'Workflow completed successfully!', color: 'success', delay: 4000 }
            ];
            
            output.innerHTML = '<div class="demo-log"></div>';
            const log = output.querySelector('.demo-log');
            
            steps.forEach((step, index) => {
                setTimeout(() => {
                    const logEntry = document.createElement('div');
                    logEntry.className = `d-flex align-items-center p-2 mb-2 rounded bg-${step.color} bg-opacity-10 border border-${step.color} border-opacity-25`;
                    logEntry.innerHTML = `
                        <i class="${step.icon} text-${step.color} me-3"></i>
                        <span>${step.text}</span>
                        <small class="ms-auto text-muted">${new Date().toLocaleTimeString()}</small>
                    `;
                    
                    logEntry.style.opacity = '0';
                    logEntry.style.transform = 'translateX(-20px)';
                    log.appendChild(logEntry);
                    
                    gsap.to(logEntry, { 
                        duration: 0.5, 
                        opacity: 1, 
                        x: 0, 
                        ease: 'power2.out' 
                    });
                }, step.delay);
            });
        }
        
        function resetDemo() {
            const output = document.getElementById('demoOutput');
            output.innerHTML = `
                <div class="text-center py-5">
                    <i class="fas fa-play-circle fa-3x text-muted mb-3"></i>
                    <p class="text-muted">Click "Run Demo" to see automation in action</p>
                </div>
            `;
        }
        
        // Workflow template selector
        document.getElementById('workflowSelect').addEventListener('change', function() {
            const workflows = {
                onboarding: [
                    { icon: 'user-plus', title: 'Trigger: New Customer Signs Up', desc: 'Automatically triggered when form is submitted', status: 'success', statusText: 'Active' },
                    { icon: 'envelope', title: 'Action: Send Welcome Email', desc: 'Personalized welcome message with getting started guide', status: 'warning', statusText: 'Processing' },
                    { icon: 'calendar', title: 'Action: Schedule Follow-up', desc: 'Book demo call after 2 days if no activity', status: 'secondary', statusText: 'Queued' }
                ],
                support: [
                    { icon: 'ticket-alt', title: 'Trigger: New Support Ticket', desc: 'Customer submits support request', status: 'success', statusText: 'Active' },
                    { icon: 'brain', title: 'Action: AI Categorization', desc: 'Automatically categorize and prioritize ticket', status: 'warning', statusText: 'Processing' },
                    { icon: 'user-tie', title: 'Action: Assign to Agent', desc: 'Route to best available specialist', status: 'secondary', statusText: 'Queued' }
                ],
                sales: [
                    { icon: 'handshake', title: 'Trigger: New Lead Captured', desc: 'Lead form submission or contact import', status: 'success', statusText: 'Active' },
                    { icon: 'chart-line', title: 'Action: Score Lead Quality', desc: 'AI analyzes lead data for qualification', status: 'warning', statusText: 'Processing' },
                    { icon: 'phone', title: 'Action: Schedule Sales Call', desc: 'Auto-book calls for high-quality leads', status: 'secondary', statusText: 'Queued' }
                ],
                hr: [
                    { icon: 'user-check', title: 'Trigger: New Hire Approved', desc: 'HR system confirms new employee', status: 'success', statusText: 'Active' },
                    { icon: 'clipboard-list', title: 'Action: Create Accounts', desc: 'Set up email, Slack, and system access', status: 'warning', statusText: 'Processing' },
                    { icon: 'graduation-cap', title: 'Action: Assign Training', desc: 'Enroll in onboarding program', status: 'secondary', statusText: 'Queued' }
                ]
            };
            
            const selectedWorkflow = workflows[this.value];
            const stepsContainer = document.getElementById('workflowSteps');
            
            stepsContainer.innerHTML = '';
            
            selectedWorkflow.forEach(step => {
                const stepElement = document.createElement('div');
                stepElement.className = 'step-item d-flex align-items-center p-3 mb-3 rounded';
                stepElement.style.background = 'var(--dark-surface)';
                stepElement.style.border = '1px solid rgba(255,255,255,0.1)';
                
                stepElement.innerHTML = `
                    <div class="step-icon me-3">
                        <div class="bg-${step.status} rounded-circle d-flex align-items-center justify-content-center" style="width: 40px; height: 40px;">
                            <i class="fas fa-${step.icon} text-white"></i>
                        </div>
                    </div>
                    <div class="flex-grow-1">
                        <h6 class="mb-1">${step.title}</h6>
                        <small class="text-muted">${step.desc}</small>
                    </div>
                    <div class="step-status">
                        <span class="badge bg-${step.status}">${step.statusText}</span>
                    </div>
                `;
                
                stepsContainer.appendChild(stepElement);
                
                gsap.from(stepElement, {
                    duration: 0.5,
                    x: -20,
                    opacity: 0,
                    delay: selectedWorkflow.indexOf(step) * 0.1,
                    ease: 'power2.out'
                });
            });
        });
        
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
        
        // Parallax effect for floating elements
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            const elements = document.querySelectorAll('.floating');
            
            elements.forEach((element, index) => {
                const speed = 0.5 + (index * 0.2);
                element.style.transform = `translateY(${scrolled * speed * 0.1}px)`;
            });
        });
        
        // Initialize animations on load
        window.addEventListener('load', () => {
            // Add subtle entrance animations
            gsap.from('body', { duration: 0.5, opacity: 0, ease: 'power2.inOut' });
        });