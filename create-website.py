import subprocess
import os

def get_framework_choice():
    while True:
        print("Choose a framework:")
        print("1. Next.js")
        print("2. Vite (Vue.js)")
        print("3. Create React App")
        print("4. Angular")
        
        framework_choice = input("Enter the number of your choice: ")

        if framework_choice in ["1", "2", "3", "4"]:
            return framework_choice
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def get_project_name():
    project_name = input("Enter the project name: ")
    if not project_name:
        project_name = "my-app"
    return project_name

def setup_nextjs(project_name):
    subprocess.run(["cmd", "/c", "pnpx create-next-app", project_name])
    os.chdir(project_name)  # Change directory in Python script

    # Create 'components' folder in 'my-app\src'
    os.makedirs("src/components", exist_ok=True)

    # Create 'contents' folder in 'my-app\src\pages'
    os.makedirs("src/pages/contents", exist_ok=True)

    subprocess.run(["cmd", "/c", "pnpm", "add", "@nextui-org/theme", "@nextui-org/system", "framer-motion"])

    with open(".npmrc", "w") as npmrc_file:
        npmrc_file.write("public-hoist-pattern[]=*@nextui-org/*\n")

    with open("tailwind.config.js", "w") as tailwind_config_file:
        tailwind_config_file.write("""
        import { nextui } from "@nextui-org/react";
        /** @type {import('tailwindcss').Config} */
        module.exports = {
        content: [
            "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
            "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
            "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
            "./node_modules/@nextui-org/theme/dist/**/*.{js,ts,jsx,tsx}",
        ],
        theme: {
            extend: {
            backgroundImage: {
                "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
                "gradient-conic": "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
            },
            },
        },
        darkMode: "class",
        plugins: [nextui()],
        };
        """)
    
    # Add the import statement to _app.js
    # with open("src/pages/_app.js", "w") as file:
    #     file.write("""
    #     // Components
    #     import '@/styles/globals.css'
    #     import { NextUIProvider } from '@nextui-org/react'
    #     import Layout from '@/components/layout'

    #     export default function App({ Component, pageProps }) {
    #     return (
    #         <NextUIProvider>
    #         <Layout>
    #             <Component {...pageProps} />
    #         </Layout>
    #         </NextUIProvider>
    #     )
    #     }
    #     """)

        print("Next.js project setup completed successfully!")

def setup_vite(project_name):
    subprocess.run(["cmd", "/c", "pnpm", "init", "vite@latest", project_name, "-e", "vue"])

def setup_create_react_app(project_name):
    subprocess.run(["cmd", "/c", "pnpx", "create-react-app", project_name])

def setup_angular(project_name):
    subprocess.run(["cmd", "/c", "ng", "new", project_name])

if __name__ == "__main__":
    framework_choice = get_framework_choice()
    project_name = get_project_name()

    print("Setting up project...")

    if framework_choice == "1":
        setup_nextjs(project_name)
    elif framework_choice == "2":
        setup_vite(project_name)
    elif framework_choice == "3":
        setup_create_react_app(project_name)
    elif framework_choice == "4":
        setup_angular(project_name)

    print("Project setup completed successfully!")
