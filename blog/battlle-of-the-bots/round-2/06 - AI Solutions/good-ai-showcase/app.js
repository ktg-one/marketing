// Good AI Website - Interactive JavaScript

class GoodAIApp {
    constructor() {
        this.chatbotOpen = false;
        this.init();
    }

    init() {
        this.setupSmoothScrolling();
        this.setupChatbot();
        this.setupScrollAnimations();
        this.setupHeaderBehavior();
    }

    // Smooth scrolling navigation
    setupSmoothScrolling() {
        const navLinks = document.querySelectorAll('.nav__link');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href');
                const targetSection = document.querySelector(targetId);
                
                if (targetSection) {
                    const headerHeight = 80;
                    const targetPosition = targetSection.offsetTop - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    // Header scroll behavior
    setupHeaderBehavior() {
        let lastScrollY = window.scrollY;
        const header = document.getElementById('header');

        window.addEventListener('scroll', () => {
            const currentScrollY = window.scrollY;
            
            if (currentScrollY > 100) {
                header.style.background = 'rgba(26, 26, 26, 0.98)';
                header.style.backdropFilter = 'blur(15px)';
            } else {
                header.style.background = 'rgba(26, 26, 26, 0.95)';
                header.style.backdropFilter = 'blur(10px)';
            }

            lastScrollY = currentScrollY;
        });
    }

    // Scroll animations
    setupScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Animate elements on scroll
        const animatedElements = document.querySelectorAll('.division-card, .service-card, .benefit, .value, .projection');
        animatedElements.forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });
    }

    // Chatbot functionality
    setupChatbot() {
        this.chatbotKnowledge = {
            welcome: "G'day! I'm the Good AI assistant, here to help you learn about our Indigenous-led digital sovereignty solutions. How can I help you today?",
            
            services: "We offer three integrated divisions:\n\n🔍 **Good AI Research** - Strategic foundation with AI readiness audits, SME workshops, and growth analytics ($5,000-$15,000)\n\n⚙️ **Good AI Technology** - Sovereign AI tools including our chatbot platform ($500/month subscription)\n\n🎨 **Good AI Creative** - Digital experiences and youth training ($2,500-$6,000)\n\nOur flagship **Digital Launchpad Package** ($13,500) includes everything you need to launch your digital presence!",
            
            sovereignty: "Indigenous Data Sovereignty means First Nations peoples have the right to own, control, and govern their own data. We built our technology on Oracle Cloud Infrastructure to ensure your data never leaves Indigenous control - no big tech giants involved!\n\nThis follows the CARE principles:\n• **Collective Benefit** - Data for community good\n• **Authority to Control** - Indigenous governance\n• **Responsibility** - Ethical data use\n• **Ethics** - Respectful practices",
            
            pricing: "Our competitive pricing includes:\n\n💎 **Digital Launchpad Package**: $13,500 (Most Popular)\n🔍 **AI Readiness Audit**: $7,000\n⚙️ **Sovereign Chatbot Platform**: $500/month\n🎨 **Web Development**: $2,500-$6,000\n\nAll services maintain cultural integrity while delivering commercial excellence. We're competitive with market rates but with Indigenous Data Sovereignty guaranteed!",
            
            values: "We operate by the **4 C's**:\n\n🤝 **Community First** - Every solution delivers tangible benefits to First Nations communities\n\n🎭 **Cultural Integrity** - We respect protocols, traditional knowledge, and cultural practices\n\n📈 **Commercial Excellence** - Sustainable profits that support long-term community impact\n\n🔐 **Control & Consent** - Indigenous Data Sovereignty is non-negotiable\n\nEverything we do starts with community benefit and ends with Indigenous control.",
            
            market: "We serve First Nations-owned businesses, Land Councils, community organizations, and any business serious about cultural protocols and data sovereignty.\n\nWith a **$3.81B total market opportunity** and **85% of SMBs experimenting with AI**, we're perfectly positioned to help organizations embrace AI while maintaining control of their digital assets.\n\nOur revenue projections: Y1 $300K, Y2 $900K, Y3 $2.1M",
            
            technology: "Our sovereign technology stack includes:\n\n🏛️ **Oracle Cloud Infrastructure** - Australian-hosted for maximum sovereignty\n⚡ **Sub-2 second response times** - Lightning-fast AI responses\n🔒 **Enterprise-grade security** - Community-controlled access\n🌏 **Local hosting** - Ensuring compliance and sovereignty\n\n99.9% uptime guaranteed, with your data never leaving Indigenous control!",
            
            contact: "Ready to start your digital sovereignty journey?\n\n📧 **Email**: hello@goodai.com.au\n📞 **Phone**: +61 x xxxx xxxx\n🏢 **ABN**: 14885784590\n\nI can help you choose the right service for your needs, or we can arrange a consultation to discuss your specific requirements. What would work best for you?"
        };

        this.setupChatbotUI();
    }

    setupChatbotUI() {
        const chatTriggers = document.querySelectorAll('.chat-trigger');
        const chatbot = document.getElementById('chatbot');
        const chatbotClose = document.getElementById('chatbot-close');
        const chatbotInput = document.getElementById('chatbot-input');
        const chatbotSend = document.getElementById('chatbot-send');
        const messagesContainer = document.getElementById('chatbot-messages');
        const quickReplies = document.querySelectorAll('.quick-reply');

        // Open chatbot
        chatTriggers.forEach(trigger => {
            trigger.addEventListener('click', () => {
                this.openChatbot();
            });
        });

        // Close chatbot
        chatbotClose.addEventListener('click', () => {
            this.closeChatbot();
        });

        // Send message on Enter key
        chatbotInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Send message on button click
        chatbotSend.addEventListener('click', () => {
            this.sendMessage();
        });

        // Quick reply buttons
        quickReplies.forEach(button => {
            button.addEventListener('click', () => {
                const message = button.getAttribute('data-message');
                this.addUserMessage(message);
                this.processUserMessage(message);
            });
        });
    }

    openChatbot() {
        const chatbot = document.getElementById('chatbot');
        chatbot.classList.remove('hidden');
        setTimeout(() => {
            chatbot.classList.add('active');
        }, 10);
        this.chatbotOpen = true;
    }

    closeChatbot() {
        const chatbot = document.getElementById('chatbot');
        chatbot.classList.remove('active');
        setTimeout(() => {
            chatbot.classList.add('hidden');
        }, 300);
        this.chatbotOpen = false;
    }

    sendMessage() {
        const input = document.getElementById('chatbot-input');
        const message = input.value.trim();
        
        if (message) {
            this.addUserMessage(message);
            input.value = '';
            this.processUserMessage(message);
        }
    }

    addUserMessage(message) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageElement = document.createElement('div');
        messageElement.className = 'message message--user';
        messageElement.innerHTML = `
            <div class="message__avatar">👤</div>
            <div class="message__content">
                <p>${message}</p>
            </div>
        `;
        messagesContainer.appendChild(messageElement);
        this.scrollToBottom();
    }

    addBotMessage(message) {
        const messagesContainer = document.getElementById('chatbot-messages');
        const messageElement = document.createElement('div');
        messageElement.className = 'message message--bot';
        messageElement.innerHTML = `
            <div class="message__avatar">🤖</div>
            <div class="message__content">
                <p>${message}</p>
            </div>
        `;
        messagesContainer.appendChild(messageElement);
        this.scrollToBottom();
    }

    processUserMessage(message) {
        // Show typing indicator
        this.showTypingIndicator();
        
        // Simulate processing time
        setTimeout(() => {
            this.hideTypingIndicator();
            const response = this.generateResponse(message);
            this.addBotMessage(response);
        }, 1000 + Math.random() * 1000); // Random delay between 1-2 seconds
    }

    generateResponse(message) {
        const messageLower = message.toLowerCase();
        
        // Service-related queries
        if (messageLower.includes('service') || messageLower.includes('what do you offer') || messageLower.includes('tell me about your services')) {
            return this.chatbotKnowledge.services;
        }
        
        // Data sovereignty queries
        if (messageLower.includes('sovereignty') || messageLower.includes('data sovereignty') || messageLower.includes('indigenous data')) {
            return this.chatbotKnowledge.sovereignty;
        }
        
        // Pricing queries
        if (messageLower.includes('price') || messageLower.includes('pricing') || messageLower.includes('cost') || messageLower.includes('how much')) {
            return this.chatbotKnowledge.pricing;
        }
        
        // Values queries
        if (messageLower.includes('value') || messageLower.includes('principle') || messageLower.includes('culture') || messageLower.includes('approach')) {
            return this.chatbotKnowledge.values;
        }
        
        // Market/business queries
        if (messageLower.includes('market') || messageLower.includes('target') || messageLower.includes('business') || messageLower.includes('opportunity')) {
            return this.chatbotKnowledge.market;
        }
        
        // Technology queries
        if (messageLower.includes('technology') || messageLower.includes('platform') || messageLower.includes('infrastructure') || messageLower.includes('technical')) {
            return this.chatbotKnowledge.technology;
        }
        
        // Contact queries
        if (messageLower.includes('contact') || messageLower.includes('reach') || messageLower.includes('phone') || messageLower.includes('email')) {
            return this.chatbotKnowledge.contact;
        }
        
        // Greeting responses
        if (messageLower.includes('hello') || messageLower.includes('hi') || messageLower.includes('hey') || messageLower.includes('g\'day')) {
            return "G'day! Great to meet you! I'm here to help you learn about Good AI's Indigenous-led digital sovereignty solutions. What would you like to know about our services, technology, or approach?";
        }
        
        // Digital Launchpad specific
        if (messageLower.includes('launchpad') || messageLower.includes('package') || messageLower.includes('comprehensive')) {
            return "Our **Digital Launchpad Package** ($13,500) is our most popular offering! It includes:\n\n✓ Complete AI Readiness Audit\n✓ Professional branding package\n✓ 5-page website development\n✓ Social media kit\n\nIt's everything you need to launch your digital presence with Indigenous Data Sovereignty at the core. Perfect for businesses ready to embrace AI while maintaining cultural integrity!";
        }
        
        // Audit specific
        if (messageLower.includes('audit') || messageLower.includes('readiness') || messageLower.includes('assessment')) {
            return "Our **AI Readiness Audit** ($7,000) analyzes your business data, processes, and objectives to identify AI integration opportunities.\n\nWe examine your current digital infrastructure, data governance practices, and business goals to create a culturally-informed strategy for AI adoption while ensuring Indigenous Data Sovereignty principles are maintained throughout.";
        }
        
        // Chatbot platform specific
        if (messageLower.includes('chatbot') || messageLower.includes('ai platform') || messageLower.includes('subscription')) {
            return "Our **Sovereign Chatbot Platform** ($500/month) offers:\n\n⚡ Sub-2 second response times\n🏛️ Oracle Cloud Infrastructure hosting\n🔒 Complete data sovereignty\n🎯 3-tier subscription service\n🌏 Australian-hosted infrastructure\n\nYour AI assistant stays under Indigenous control - no big tech giants involved! Perfect for businesses wanting AI capabilities without compromising on data sovereignty.";
        }
        
        // Default response with helpful suggestions
        return "That's a great question! I can help you with information about:\n\n🔍 Our three divisions (Research, Technology, Creative)\n💰 Pricing and service packages\n🏛️ Indigenous Data Sovereignty\n⚙️ Our technology platform\n🎯 Our cultural values and approach\n📞 How to get in touch\n\nWhat would you like to learn more about?";
    }

    showTypingIndicator() {
        const messagesContainer = document.getElementById('chatbot-messages');
        const typingElement = document.createElement('div');
        typingElement.className = 'message message--bot typing-indicator';
        typingElement.innerHTML = `
            <div class="message__avatar">🤖</div>
            <div class="message__content">
                <p>Good AI assistant is typing...</p>
            </div>
        `;
        messagesContainer.appendChild(typingElement);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        const typingIndicator = document.querySelector('.typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }

    scrollToBottom() {
        const messagesContainer = document.getElementById('chatbot-messages');
        setTimeout(() => {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }, 100);
    }
}

// Enhanced smooth scrolling for all internal links
document.addEventListener('DOMContentLoaded', function() {
    // Initialize the app
    const app = new GoodAIApp();
    
    // Enhanced button interactions
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 8px 25px rgba(210, 105, 30, 0.3)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = 'none';
        });
    });
    
    // Enhanced card hover effects
    const cards = document.querySelectorAll('.division-card, .service-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.hero__pattern');
        if (parallax) {
            const speed = scrolled * 0.5;
            parallax.style.transform = `translateY(${speed}px)`;
        }
    });
    
    // Stats counter animation
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const statNumbers = entry.target.querySelectorAll('.stat__number, .projection__revenue');
                statNumbers.forEach(stat => {
                    const text = stat.textContent;
                    if (text.includes('$') || text.includes('%') || text.includes('+')) {
                        animateValue(stat, text);
                    }
                });
                statsObserver.unobserve(entry.target);
            }
        });
    });
    
    const heroStats = document.querySelector('.hero__stats');
    const projectionCharts = document.querySelectorAll('.projections__chart');
    
    if (heroStats) statsObserver.observe(heroStats);
    projectionCharts.forEach(chart => statsObserver.observe(chart));
    
    function animateValue(element, finalText) {
        element.style.opacity = '0';
        setTimeout(() => {
            element.textContent = finalText;
            element.style.opacity = '1';
            element.style.transform = 'scale(1.1)';
            setTimeout(() => {
                element.style.transform = 'scale(1)';
            }, 200);
        }, Math.random() * 500);
    }
    
    // Loading animation for the page
    document.body.style.opacity = '0';
    window.addEventListener('load', () => {
        document.body.style.transition = 'opacity 0.5s ease';
        document.body.style.opacity = '1';
    });
    
    // Mobile menu toggle (if needed)
    const createMobileMenu = () => {
        const nav = document.querySelector('.nav');
        const menu = document.querySelector('.nav__menu');
        
        if (window.innerWidth <= 768) {
            if (!document.querySelector('.nav__toggle')) {
                const toggle = document.createElement('button');
                toggle.className = 'nav__toggle';
                toggle.innerHTML = '☰';
                toggle.style.cssText = `
                    background: none;
                    border: none;
                    color: var(--color-warm-white);
                    font-size: 1.5rem;
                    cursor: pointer;
                    padding: 8px;
                `;
                
                toggle.addEventListener('click', () => {
                    menu.style.display = menu.style.display === 'flex' ? 'none' : 'flex';
                    if (menu.style.display === 'flex') {
                        menu.style.position = 'absolute';
                        menu.style.top = '100%';
                        menu.style.left = '0';
                        menu.style.right = '0';
                        menu.style.background = 'var(--color-background)';
                        menu.style.flexDirection = 'column';
                        menu.style.padding = '16px';
                        menu.style.borderTop = '2px solid var(--color-primary)';
                    }
                });
                
                nav.insertBefore(toggle, nav.lastElementChild);
            }
        }
    };
    
    createMobileMenu();
    window.addEventListener('resize', createMobileMenu);
});